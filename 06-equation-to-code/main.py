from pathlib import Path
from datasets import load_from_disk, load_dataset
import torch
from latex2sympy2_extended import latex2sympy



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


for data in dataloader:
    data['images'][0].show()
    print(data['sympy_formulas'][0])
    exit()
