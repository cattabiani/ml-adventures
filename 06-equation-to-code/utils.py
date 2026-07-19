import sympy as sp
import torch

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
            for idx in range(len(seq) - 1):
                if seq[idx] == 151644 and seq[idx+1] == 77091:
                    labels[i, :idx+2] = -100
                    break
            
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
    ground_truths = data["sympy_formulas"]
    correct = 0
    total = len(ground_truths)
    
    for pred, gt in zip(predictions, ground_truths):
        try:
            pred_expr = sp.sympify(pred.strip())
            gt_expr = sp.sympify(gt)
            
            # Check algebraic equivalence
            is_equivalent = sp.simplify(pred_expr - gt_expr) == 0
            if is_equivalent:
                correct += 1
            print(f"Prediction: {pred} | GT: {gt} | Equivalent: {is_equivalent}")
        except Exception as e:
            print(f"Failed to parse prediction '{pred}': {e}")
            
    return correct, total
