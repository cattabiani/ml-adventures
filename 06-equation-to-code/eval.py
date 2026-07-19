import os
import glob
from pathlib import Path
import torch
from datasets import load_from_disk
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor, BitsAndBytesConfig
from peft import PeftModel
from utils import collate_fn, preprocess_batch, postproc_output_ids, compare

model_id = "Qwen/Qwen2-VL-2B-Instruct"
device = "cuda" if torch.cuda.is_available() else "cpu"

batch_size = 8

def main():
    processed_path = Path("data/synthetic_dataset")
    dataset = load_from_disk(str(processed_path))
    
    # 1. Split the dataset (ensure same seed=42) and get the eval/test split
    dataset = dataset.train_test_split(test_size=0.1, seed=42)
    train_data = dataset['train']
    eval_data = dataset['test']
    
    # 2. Initialize processor and dataloader (batch_size 4 or 8 is safe)
    dataloader = torch.utils.data.DataLoader(eval_data, batch_size=batch_size, collate_fn=collate_fn)
    processor = AutoProcessor.from_pretrained(model_id)
    
    # 3. Load base model in 4-bit (reuse the same BitsAndBytesConfig as training)
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4"
    )
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        model_id,
        quantization_config=quantization_config,
        device_map="auto"
    )

    # 4. Check if adapter checkpoints exist in "data/lora_finetuning"
    # If they do, load the latest one onto the base model using PeftModel
    adapter_path = "data/lora_finetuning"
    checkpoints = glob.glob(os.path.join(adapter_path, "checkpoint-*"))
    if checkpoints:
        latest_checkpoint = max(checkpoints, key=os.path.getctime)
        print(f"Loading trained adapter from: {latest_checkpoint}")
        model = PeftModel.from_pretrained(model, latest_checkpoint)
    else:
        print("No adapters found. Evaluating the zero-shot base model.")
    
    model.eval()

    correct = 0
    n_tests = 0
    for data in dataloader:
        inputs = preprocess_batch(processor, data, is_train=False).to(device)
        output_ids = model.generate(**inputs, max_new_tokens=100)
        predictions = postproc_output_ids(processor, inputs, output_ids)
        corr, tot = compare(predictions, data)
        correct += corr
        n_tests += tot
        


    print(f"Final evaluation (%): {100*correct/n_tests}")


if __name__ == "__main__":
    main()
