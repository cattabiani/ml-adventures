from pathlib import Path
from datasets import load_from_disk, load_dataset
import torch
from latex2sympy2_extended import latex2sympy
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor, BitsAndBytesConfig, TrainingArguments, Trainer
model_id = "Qwen/Qwen2-VL-2B-Instruct"
import sympy as sp
from peft import LoraConfig, TaskType
from peft import get_peft_model


def collate_fn(batch):
    return {
        "images": [item["image"] for item in batch],
        "sympy_formulas": [item["sympy_formula"] for item in batch],
    }


def preprocess_batch(processor, data, is_train):
    if is_train: 
        messages_batch = [
            [
                {
                    "role": "user",
                    "content": [
                        {"type": "image", "image": img},
                        {"type": "text", "text": "Convert this equation into Python code."},
                        
                    ],
                },
                {
                    "role": "assistant",
                    "content": [
                        {"type": "text", "text": ans},
                    ]
                }
            ]
            for img, ans in zip(data["images"], data["sympy_formulas"])
        ]
    else:
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
            for img, ans in zip(data["images"], data["sympy_formulas"])
        ]
    texts = [
        processor.apply_chat_template(m, tokenize=False, add_generation_prompt=(not is_train))
        for m in messages_batch
    ]

    inputs = processor(
        text=texts,
        images=data["images"],
        padding=True,
        return_tensors="pt"
    )
    if is_train:
        # 1. Start by cloning the input_ids
        labels = inputs["input_ids"].clone()
        
        # 2. Iterate through each sequence in the batch
        for i in range(labels.shape[0]):
            seq = labels[i].tolist()
            for idx in range(len(seq) -1):
                if seq[idx] == 151644 and seq[idx+1] == 77091:
                    labels[i, :idx+2] = -100
                    break
            # We want to find where the sequence [151644, 77091] (<|im_start|>assistant) is located in labels[i]
            # Once found at index j, set labels[i, :j + 2] = -100
            
        # 3. Add the masked labels back to the inputs dictionary
        labels[inputs["attention_mask"] == 0] = -100
        inputs["labels"] = labels
        



    return inputs

def postproc_output_ids(processor, inputs, output_ids):
    # Trim the prompt tokens
    generated_ids_trimmed = [
        out_ids[len(in_ids):] 
        for in_ids, out_ids in zip(inputs.input_ids, output_ids)
    ]
    # Decode the output
    predictions = processor.batch_decode(
        generated_ids_trimmed, 
        skip_special_tokens=True, 
        clean_up_tokenization_spaces=False
    )
    return predictions

def compare(predictions, data):
    # 2. Compare with ground truths
    ground_truths = data["sympy_formulas"]
    
    for pred, gt in zip(predictions, ground_truths):
        try:
            pred_expr = sp.sympify(pred.strip())
            gt_expr = sp.sympify(gt)
            
            # Check algebraic equivalence
            is_equivalent = sp.simplify(pred_expr - gt_expr) == 0
            print(f"Prediction: {pred} | GT: {gt} | Equivalent: {is_equivalent}")
        except Exception as e:
            print(f"Failed to parse prediction '{pred}': {e}")


device = 'cuda' if torch.cuda.is_available() else 'cpu'
torch.manual_seed(1337)

## hyperparameters

batch_size = 32
processed_path = Path("data/synthetic_dataset")

## /hyperparameters

dataset = load_from_disk(str(processed_path))


dataset = dataset.train_test_split(test_size=0.1, seed=42)
train_data = dataset['train']
eval_data = dataset['test']

dataloader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)




# Configure 4-bit quantization
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4"
)


peft_config = LoraConfig(task_type=TaskType.CAUSAL_LM, 
                inference_mode=False, 
                r=8, 
                lora_alpha=32, 
                lora_dropout=0.1,
                target_modules=["q_proj", "k_proj", "v_proj", "o_proj"]
                )


# Load model and processor
model = Qwen2VLForConditionalGeneration.from_pretrained(
    model_id,
    quantization_config=quantization_config,
    device_map="auto"
)
model = get_peft_model(model, peft_config)
model.print_trainable_parameters()


training_args = TrainingArguments(
    output_dir="data/lora_finetuning",
    learning_rate=2e-4,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=16,
    per_device_eval_batch_size=2,
    optim="paged_adamw_8bit",
    num_train_epochs=2,
    weight_decay=0.01,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)
processor = AutoProcessor.from_pretrained(model_id)
def data_collator(data):
    return preprocess_batch(processor, collate_fn(data), is_train=True)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=eval_data,
    processing_class=processor.tokenizer,
    data_collator=data_collator,
)

trainer.train()


exit()






for data in dataloader:
    inputs = preprocess_batch(processor, data)
    output_ids = model.generate(**inputs.to(device), max_new_tokens=100)
    predictions = postproc_output_ids(processor, inputs, output_ids)
    compare(predictions, data)
    exit()