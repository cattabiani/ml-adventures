from pathlib import Path
from datasets import load_from_disk, load_dataset
import torch
from latex2sympy2_extended import latex2sympy
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor, BitsAndBytesConfig
from qwen_vl_utils import process_vision_info
model_id = "Qwen/Qwen2-VL-2B-Instruct"


def collate_fn(batch):
    return {
        "images": [item["image"] for item in batch],
        "sympy_formulas": [item["sympy_formula"] for item in batch],
    }


def preprocess_batch(processor, data):
    messages_batch = [
        [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": img},
                    {"type": "text", "text": "Convert this equation into Python code."},
                ],
            }
        ]
        for img in data["images"]
    ]
    texts = [
        processor.apply_chat_template(m, tokenize=False, add_generation_prompt=True)
        for m in messages_batch
    ]
    image_inputs, video_inputs = process_vision_info(messages)
    text_inputs = processor(
        text=texts,
        images=data["images"],
        padding=True,
        return_tensors="pt"
    )
    return text_inputs, image_inputs, video_inputs


device = 'cuda' if torch.cuda.is_available() else 'cpu'
torch.manual_seed(1337)

## hyperparameters

batch_size = 32
processed_path = Path("data/synthetic_dataset")

## /hyperparameters

dataset = load_from_disk(str(processed_path))


dataset = dataset.train_test_split(test_size=0.1, seed=42)
train_data = dataset['train']
val_data = dataset['test']

dataloader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)




# Configure 4-bit quantization
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4"
)
# Load model and processor
model = Qwen2VLForConditionalGeneration.from_pretrained(
    model_id,
    quantization_config=quantization_config,
    device_map="auto"
)
processor = AutoProcessor.from_pretrained(model_id)

for data in dataloader:
    text_inputs, image_inputs, video_inputs = preprocess_batch(processor, data)
    inputs = processor(
        text=text_inputs,
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt"
    )
    output_ids = model.generate(**inputs.to(device), max_new_tokens=100)
    exit()