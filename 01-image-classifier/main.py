import torch
import torchvision

from torchvision.transforms import v2
from pathlib import Path

data_path = Path("./data").absolute()

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"device: {device}")

def inspect_obj(obj):
    """General-purpose inspector for any object."""
    print(f"Type: {type(obj).__name__}")
    print(f"Repr: {repr(obj)[:200]}")
    if hasattr(obj, '__len__'):
        print(f"Len:  {len(obj)}")
    if hasattr(obj, 'shape'):
        print(f"Shape: {obj.shape}")
    if hasattr(obj, 'dtype'):
        print(f"Dtype: {obj.dtype}")
    if hasattr(obj, 'size') and callable(obj.size):
        print(f"Size: {obj.size()}")
    elif hasattr(obj, 'size'):
        print(f"Size: {obj.size}")
    if hasattr(obj, 'mode'):
        print(f"Mode: {obj.mode}")
    # Show public attributes and methods
    members = [m for m in dir(obj) if not m.startswith('_')]
    print(f"Members ({len(members)}): {members[:20]}")
    if len(members) > 20:
        print(f"  ... and {len(members) - 20} more")

epochs = 40


class CNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1)
        self.conv2 = torch.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1)
        self.linear = torch.nn.Linear(in_features=int(32*8*8), out_features=10)
        self.dropout = torch.nn.Dropout(0.2)

    def forward(self, x):
        x = self.conv1(x)
        x = torch.nn.functional.relu(x)
        x = torch.nn.functional.max_pool2d(x, kernel_size=2)
        x = self.conv2(x)
        x = torch.nn.functional.relu(x)
        x = torch.nn.functional.max_pool2d(x, kernel_size=2)
        x = x.flatten(start_dim=1)
        x = self.dropout(x)
        x = self.linear(x)
        return x


transform_to_tensor = v2.Compose([v2.PILToTensor(), v2.ToDtype(torch.float32, scale=True)])
train_transform_to_tensor = v2.Compose([v2.PILToTensor(), v2.ToDtype(torch.float32, scale=True), v2.RandomCrop(32, padding=4), v2.RandomHorizontalFlip()])
ds_train = torchvision.datasets.CIFAR10(root=data_path, train=True, transform=train_transform_to_tensor, download=True)
ds_test = torchvision.datasets.CIFAR10(root=data_path, train=False, transform=transform_to_tensor, download=True)

dl_train = torch.utils.data.DataLoader(dataset=ds_train, batch_size=64, shuffle=True)
dl_test = torch.utils.data.DataLoader(dataset=ds_test, batch_size=64, shuffle=False)

model = CNN().to(device)
loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

model.train()
for epoch in range(epochs):
    err = 0
    for batch, target in dl_train:
        batch, target = batch.to(device), target.to(device)
        optimizer.zero_grad()
        loss = loss_fn(model(batch), target)
        err += loss.item()
        loss.backward()
        optimizer.step()

    err /= len(dl_train)

    print(f"Epoch {epoch+1}/{epochs}, err: {err}")

test_correct = 0
train_correct = 0
model.eval()
with torch.no_grad():
    for batch, target in dl_test:
        batch, target = batch.to(device), target.to(device)
        ans = torch.argmax(model(batch), dim=1)
        test_correct += (target == ans).sum().item()
    for batch, target in dl_train:
        batch, target = batch.to(device), target.to(device)
        ans = torch.argmax(model(batch), dim=1)
        train_correct += (target == ans).sum().item()

print(f"Train accuracy: {100*train_correct/len(ds_train)}%")
print(f"Test accuracy: {100*test_correct/len(ds_test)}%")
