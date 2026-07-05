# Character-Level GPT — Task Breakdown

## Tasks

### Task 1: Understand attention [x]
- What is self-attention? (query, key, value) [x]
- Why does it work? (every token can look at every other token) [x]
- Multi-head attention (parallel attention with different learned projections) [x]
- Causal masking (can only look at past tokens, not future) [x]

### Task 2: Data pipeline [x]
- Pick a text corpus (Shakespeare, code, Wikipedia — small, ~1MB) [x]
- Character-level tokenization (no tokenizer library needed) [x]
- Batch sequences into fixed-length chunks [x]
- Train/val split [x]

### Task 3: Build the transformer [x]
- Token embedding + positional embedding [x]
- Transformer block: multi-head self-attention → add & norm → feedforward → add & norm [x]
- Stack N blocks [x]
- Final linear layer → logits over vocabulary (characters) [x]

### Task 4: Training [x]
- Cross-entropy loss (next character prediction) [x]
- Train on GPU (local RTX 4070 Ti with CUDA, or Kaggle/Colab) [x]
- Track train/val loss [x]
- Generate sample text periodically to see progress [x]

### Task 5: Generation [x]
- Autoregressive sampling: feed context, sample next character, append, repeat [x]
- Temperature control (higher = more random, lower = more deterministic) [ ]
- Generate text and evaluate quality subjectively [x]

### Task 6: Scale experiments [ ]
- Try different model sizes (layers, heads, embedding dim) [ ]
- Compare training time vs quality [ ]
- Understand the scaling behavior [ ]

## Infrastructure
- Develop on Mac, train on PC (RTX 4070 Ti, 12GB VRAM, CUDA) or Kaggle/Colab
- Learn to move code between machines, manage GPU training
