import torch


device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)

torch.manual_seed(1337)

# hyper parameters

batch_size = 32
block_size = 8
learning_rate = 1e-3
max_iters = 5000
eval_interval = 300
eval_iters = 200
n_embed = 32
# data
with open('data/input.txt','r', encoding='utf-8') as f:
    text = f.read()

chars = sorted(list(set(text + '1234567890')))
vocabular_size = len(chars)

stoi = {c: idx for idx, c in enumerate(chars)}
itos = {idx: c for idx, c in enumerate(chars)}
def encode(s):
    return [stoi[c] for c in s]
def decode(l):
    return ''.join([itos[idx] for idx in l])


# train and test splits
data = torch.tensor(encode(text), dtype=torch.long)
n = int(len(data)*0.9)
train_data = data[:n]
val_data = data[n:]


# data loading
def get_batch(split):
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    x, y = x.to(device), y.to(device)
    return x, y

class Head(torch.nn.Module):
    def __init__(self, head_size):
        super().__init__()
        self.kW = torch.nn.Linear(n_embed, head_size, bias=False)
        self.qW = torch.nn.Linear(n_embed, head_size, bias=False)
        self.vW = torch.nn.Linear(n_embed, head_size, bias=False)
        self.register_buffer('tril', torch.tril(torch.ones(block_size, block_size)))

    def forward(self, x):
        B, T, C = x.shape
        K = self.kW(x)
        Q = self.qW(x)
        V = self.vW(x)

        wei = Q @ K.transpose(-2, -1) * K.shape[-1]**-0.5
        wei = wei.masked_fill(self.tril[:T, :T] == 0, float('-inf'))
        wei = torch.nn.functional.softmax(wei, dim=-1)

        out = wei @ V
        return out

class MultiHead(torch.nn.Module):
    def __init__(self, num_heads, head_size):
        super().__init__()
        self.heads = torch.nn.ModuleList([Head(head_size) for _ in range(num_heads)])

    def forward(self, x):
        return torch.cat([h(x) for h in self.heads], dim=-1)

    


# model
class BigramLM(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.token_embedding_table = torch.nn.Embedding(vocabular_size, n_embed)
        self.position_embedding_table = torch.nn.Embedding(block_size, n_embed)
        self.sa_heads = MultiHead(4, n_embed//4)
        self.lm_head = torch.nn.Linear(n_embed, vocabular_size)
    
    def forward(self, idxs, targets=None):
        B, T = idxs.shape
        pos_embeds = self.position_embedding_table(torch.arange(T, device=device))
        token_embeds = self.token_embedding_table(idxs) # (B, T, C)
        x = token_embeds+pos_embeds
        x = self.sa_heads(x)
        logits = self.lm_head(x) # (B, T, vocab_size)
        B, T, C = logits.shape
        logits2 = logits.view(B*T, C)
        if targets is None:
            return logits, None
        targets = targets.view(B*T)        
        loss = torch.nn.functional.cross_entropy(logits2, targets)
        return logits, loss #(B*T, C)

    def generate(self, idx, max_new_tokens):
        # idx is (B, T)
        for _ in range(max_new_tokens):
            idx_cond = idx[:, -block_size:]
            logits, _loss = self(idx_cond)
            last_char = logits[:, -1, :]
            probs = torch.nn.functional.softmax(last_char, dim=1)
            idx_next = torch.multinomial(probs, num_samples=1)
            idx = torch.cat((idx, idx_next), dim=1)
        return idx


@torch.no_grad()
def estimate_loss():
    out = {}
    m.eval()
    for split in ['train', 'val']:
        losses = torch.zeros(eval_iters)
        for k in range(eval_iters):
            X, Y = get_batch(split)
            _, loss = m(X, Y)
            losses[k] = loss.item()
        out[split] = losses.mean()
    m.train()
    return out

# training

m = BigramLM().to(device)
optimizer = torch.optim.AdamW(m.parameters(), lr=learning_rate)

for iter in range(max_iters):
    xb, yb = get_batch('train')
    optimizer.zero_grad(set_to_none=True)
    logits, loss = m(xb, yb)
    loss.backward()
    optimizer.step()
    if iter%eval_interval == 0:
        losses = estimate_loss()
        print(f"step {iter}: train loss {losses['train']:.4f} val loss {losses['val']:.4f}")

context = torch.zeros((1,1), dtype=torch.long, device=device)
l = m.generate(context, max_new_tokens=500)
print(decode(l[0].tolist()))
