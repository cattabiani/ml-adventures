# Equation-to-Code — Task Breakdown

## Tasks

### Task 1: Data Generation Pipeline
- Set up a script to parse LaTeX equations and translate them to SymPy/Python expressions using `latex2sympy2` [ ]
- Write a renderer script (using matplotlib or sympy.preview) to convert LaTeX strings into PNG images [ ]
- Package the generated images and code strings into a Hugging Face Dataset format [ ]

### Task 2: Environment & Base Model Setup
- Install dependencies: `transformers`, `peft`, `trl`, `latex2sympy2`, `sympy`, `accelerate`, `bitsandbytes` [ ]
- Load a small VLM (e.g., `Qwen/Qwen2-VL-2B-Instruct`) and verify zero-shot performance on a sample equation image [ ]

### Task 3: QLoRA Fine-Tuning
- Configure QLoRA parameters (4-bit quantization, rank, alpha, target modules) [ ]
- Write the training script using Hugging Face `SFTTrainer` or a custom PyTorch loop [ ]
- Set up gradient checkpointing and memory optimization [ ]

### Task 4: Training & Monitoring
- Train the model locally on the RTX 4070 Ti [ ]
- Log training and validation loss [ ]

### Task 5: Evaluation & Inference
- Build an inference script that takes a new image and generates Python code [ ]
- Test on unseen typeset equation images and evaluate execution correctness [ ]
