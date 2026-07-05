# 06 — Equation-to-Code Converter

A Vision-Language Model (VLM) fine-tuned to translate images of mathematical equations into executable Python code (SymPy/NumPy).

## Goal

Fine-tune a pre-trained Vision-Language Model (e.g., Qwen2-VL-2B) using QLoRA to parse images of typeset math equations (such as calculus, algebra, and matrices) and generate equivalent, executable Python code.

## Methodology

1. **Synthetic Data Generation:** Render LaTeX math formulas from a text corpus (e.g., `OleehyO/latex-formulas`) into PNG images.
2. **Target Mapping:** Convert the LaTeX source strings into executable Python expressions using `latex2sympy2`.
3. **QLoRA Fine-Tuning:** Load a small pre-trained VLM in 4-bit, attach LoRA adapters, and train on the image-to-code pairs.
4. **Evaluation:** Measure syntax accuracy and symbolic equivalence of the generated code.

## Status

In progress (Setting up data generation pipeline)

## Results

*TBD*
