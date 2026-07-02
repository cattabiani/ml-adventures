# Character-Level GPT — Task Breakdown

## Tasks

### Task 1: Understand attention
- What is self-attention? (query, key, value)
- Why does it work? (every token can look at every other token)
- Multi-head attention (parallel attention with different learned projections)
- Causal masking (can only look at past tokens, not future)

### Task 2: Data pipeline
- Pick a text corpus (Shakespeare, code, Wikipedia — small, ~1MB)
- Character-level tokenization (no tokenizer library needed)
- Batch sequences into fixed-length chunks
- Train/val split

### Task 3: Build the transformer
- Token embedding + positional embedding
- Transformer block: multi-head self-attention → add & norm → feedforward → add & norm
- Stack N blocks
- Final linear layer → logits over vocabulary (characters)

### Task 4: Training
- Cross-entropy loss (next character prediction)
- Train on GPU (local RTX 4070 Ti with CUDA, or Kaggle/Colab)
- Track train/val loss
- Generate sample text periodically to see progress

### Task 5: Generation
- Autoregressive sampling: feed context, sample next character, append, repeat
- Temperature control (higher = more random, lower = more deterministic)
- Generate text and evaluate quality subjectively

### Task 6: Scale experiments
- Try different model sizes (layers, heads, embedding dim)
- Compare training time vs quality
- Understand the scaling behavior

## Infrastructure
- Develop on Mac, train on PC (RTX 4070 Ti, 12GB VRAM, CUDA) or Kaggle/Colab
- Learn to move code between machines, manage GPU training
