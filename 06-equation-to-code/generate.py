import io
import random
from pathlib import Path
import matplotlib.pyplot as plt
import sympy as sp
from PIL import Image
from datasets import Dataset

def render_latex(latex_str):
    # Strip \limits to make it compatible with Matplotlib
    clean_latex = latex_str.replace(r'\limits', '')
    
    fig = plt.figure(figsize=(6, 2), dpi=200)
    plt.text(0.5, 0.5, f"${clean_latex}$", size=20, ha='center', va='center')
    plt.axis('off')
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.1, transparent=True)
    plt.close(fig)
    
    buf.seek(0)
    return Image.open(buf)

def generate_expression(depth=0, max_depth=3):
    x, y, i = sp.symbols('x y i')
    leaves = [x, y, i, sp.Integer(random.randint(1, 9))]
    
    if depth >= max_depth:
        return random.choice(leaves)
    
    op = random.choice(['add', 'mul', 'pow', 'sin', 'cos', 'derivative', 'integral', 'sum'])
    
    if op == 'add':
        return generate_expression(depth + 1, max_depth) + generate_expression(depth + 1, max_depth)
    elif op == 'mul':
        return generate_expression(depth + 1, max_depth) * generate_expression(depth + 1, max_depth)
    elif op == 'pow':
        return generate_expression(depth + 1, max_depth) ** random.randint(2, 4)
    elif op == 'sin':
        return sp.sin(generate_expression(depth + 1, max_depth))
    elif op == 'cos':
        return sp.cos(generate_expression(depth + 1, max_depth))
    elif op == 'derivative':
        return sp.Derivative(generate_expression(depth + 1, max_depth), x)
    elif op == 'integral':
        return sp.Integral(generate_expression(depth + 1, max_depth), (x, 0, 5))
    elif op == 'sum':
        return sp.Sum(generate_expression(depth + 1, max_depth), (i, 1, 10))

# Generate dataset
num_samples = 1000
images = []
sympy_formulas = []
latex_formulas = []

print("Generating synthetic dataset...")
for _ in range(num_samples):
    expr = generate_expression()
    latex_code = sp.latex(expr)
    
    images.append(render_latex(latex_code))
    sympy_formulas.append(str(expr))
    latex_formulas.append(latex_code)

# Package into Hugging Face Dataset
dataset = Dataset.from_dict({
    "image": images,
    "sympy_formula": sympy_formulas,
    "latex_formula": latex_formulas
})

# Save to disk
out_dir = Path("data/synthetic_dataset")
dataset.save_to_disk(str(out_dir))
print(f"Generated {num_samples} samples and saved to {out_dir}")
