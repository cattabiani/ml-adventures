from pathlib import Path
from datasets import load_from_disk, load_dataset
import torch
from latex2sympy2_extended import latex2sympy
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor, BitsAndBytesConfig, TrainingArguments, Trainer
model_id = "Qwen/Qwen2-VL-2B-Instruct"
import sympy as sp
from peft import LoraConfig, TaskType
from peft import get_peft_model


from utils import collate_fn, preprocess_batch, postproc_output_ids, compare


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
    remove_unused_columns=False,
)
processor = AutoProcessor.from_pretrained(model_id)
def data_collator(data):
    return preprocess_batch(processor, collate_fn(data), is_train=True)

# help(TrainingArguments)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=eval_data,
    processing_class=processor.tokenizer,
    data_collator=data_collator,
)

trainer.train()


# for data in dataloader:
#     inputs = preprocess_batch(processor, data)
#     output_ids = model.generate(**inputs.to(device), max_new_tokens=100)
#     predictions = postproc_output_ids(processor, inputs, output_ids)
#     compare(predictions, data)
#     exit()