import torch

B, T, C = 4, 8, 32

x = torch.randn(B, T, C)
head_size = 16
key_W = torch.nn.Linear(C, head_size, bias=False)
query_W = torch.nn.Linear(C, head_size, bias=False)
value_W = torch.nn.Linear(C, head_size, bias=False)
K = key_W(x) # ( B, T, head_size)
Q = query_W(x) # ( B, T, head_size)
V = value_W(x)

wei = Q @ K.transpose(-2, -1) * head_size**-0.5
tril = torch.tril(torch.ones(T, T))
wei = wei.masked_fill(tril==0, float('-inf'))
wei = torch.nn.functional.softmax(wei, dim=-1)
out = wei @ V


print(out.shape)