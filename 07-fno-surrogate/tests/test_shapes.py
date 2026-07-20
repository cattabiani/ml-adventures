import pytest
import torch
from src.models import FNO2d
from src.training import RelativeL2Loss

def test_fno2d_shape():
    # Batch size of 2, 5 channels (E, fx, fy, x_coord, y_coord), 32x32 grid
    batch_size = 2
    in_channels = 5
    out_channels = 3
    h, w = 32, 32
    
    model = FNO2d(
        in_channels=in_channels,
        out_channels=out_channels,
        modes1=12,
        modes2=12,
        width=32
    )
    
    x = torch.randn(batch_size, in_channels, h, w)
    out = model(x)
    
    assert out.shape == (batch_size, out_channels, h, w)


def test_relative_l2_loss():
    criterion = RelativeL2Loss()
    
    pred = torch.randn(4, 3, 32, 32)
    target = torch.randn(4, 3, 32, 32)
    
    loss = criterion(pred, target)
    
    # Assert loss is a scalar tensor
    assert loss.dim() == 0
    assert not torch.isnan(loss)
