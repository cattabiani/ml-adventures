from pathlib import Path
from datasets import load_from_disk, load_dataset
import torch
from latex2sympy2_extended import latex2sympy
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor, BitsAndBytesConfig
model_id = "Qwen/Qwen2-VL-2B-Instruct"


def collate_fn(batch):
    return {
        "images": [item["image"] for item in batch],
        "sympy_formulas": [item["sympy_formula"] for item in batch],
    }


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


# for data in dataloader:
#     data['images'][0].show()
#     print(data['sympy_formulas'][0])
#     exit()



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
print("Model loaded successfully in 4-bit.")

# Take a sample from the validation set
sample = val_data[0]
image = sample["image"]
ground_truth = sample["sympy_formula"]

# Format the message
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": "Identify the mathematical expression in this image and write it in SymPy syntax."}
        ]
    }
]
text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = processor(
    text=[text],
    images=[image],
    padding=True,
    return_tensors="pt"
).to("cuda")

# Generate
print("Running zero-shot inference...")
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)[0]

print(f"\nGround Truth: {ground_truth}")
print(f"Zero-Shot Prediction: {output_text}\n")