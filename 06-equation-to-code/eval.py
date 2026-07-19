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
    
    # 1. Split the dataset (ensure same seed=42) and get the eval/test split
    # TODO
    
    # 2. Initialize processor and dataloader (batch_size 4 or 8 is safe)
    # TODO
    
    # 3. Load base model in 4-bit (reuse the same BitsAndBytesConfig as training)
    # TODO
    
    # 4. Check if adapter checkpoints exist in "data/lora_finetuning"
    # If they do, load the latest one onto the base model using PeftModel
    # TODO
    
    # 5. Set model to eval mode and run the inference loop over the dataloader
    # - call preprocess_batch(..., is_train=False)
    # - generate predictions with model.generate()
    # - decode predictions with postproc_output_ids()
    # - calculate algebraic equivalence accuracy using compare()
    # TODO
    
    # 6. Print final validation accuracy metrics
    # TODO

if __name__ == "__main__":
    main()
