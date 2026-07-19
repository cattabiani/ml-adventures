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

def main():
    processed_path = Path("data/synthetic_dataset")
    dataset = load_from_disk(str(processed_path))
    
    # Use the same split seed as training to evaluate on the correct test split
    dataset = dataset.train_test_split(test_size=0.1, seed=42)
    eval_data = dataset['test']
    
    # Initialize processor
    processor = AutoProcessor.from_pretrained(model_id)
    
    # DataLoader for evaluation
    dataloader = torch.utils.data.DataLoader(
        eval_data, 
        batch_size=8, 
        shuffle=False, 
        collate_fn=collate_fn
    )
    
    # Configure 4-bit quantization (same as training to fit in VRAM)
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4"
    )
    
    print("Loading base model...")
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        model_id,
        quantization_config=quantization_config,
        device_map="auto"
    )
    
    # Check if a trained adapter checkpoint exists
    adapter_path = "data/lora_finetuning"
    checkpoints = glob.glob(os.path.join(adapter_path, "checkpoint-*"))
    if checkpoints:
        latest_checkpoint = max(checkpoints, key=os.path.getctime)
        print(f"Loading trained adapter from: {latest_checkpoint}")
        model = PeftModel.from_pretrained(model, latest_checkpoint)
    else:
        print("No adapters found. Evaluating the zero-shot base model.")
        
    model.eval()
    
    total_correct = 0
    total_samples = 0
    
    print("\nStarting evaluation...")
    with torch.no_grad():
        for batch in dataloader:
            # We use is_train=False to not include the ground truth in the prompt
            inputs = preprocess_batch(processor, batch, is_train=False)
            
            # Move inputs to device (and handle dtype casting if necessary)
            inputs = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}
            
            # Generate the predicted sequence
            output_ids = model.generate(**inputs, max_new_tokens=100)
            
            # Post-process output IDs to extract prediction strings
            predictions = postproc_output_ids(processor, inputs, output_ids)
            
            # Compare predictions with ground truth SymPy formulas
            correct, total = compare(predictions, batch)
            
            total_correct += correct
            total_samples += total
            
    accuracy = (total_correct / total_samples) * 100 if total_samples > 0 else 0
    print(f"\nEvaluation Complete.")
    print(f"Total Samples: {total_samples}")
    print(f"Algebraically Equivalent: {total_correct}")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
