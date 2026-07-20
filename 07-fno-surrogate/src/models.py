import torch
import torch.nn as nn

class SpectralConv2d(nn.Module):
    """
    2D Fourier/Spectral Convolution layer.
    Transforms spatial inputs to the frequency domain via 2D FFT,
    filters/multiplies low-frequency modes, and projects back via 2D IFFT.
    """
    def __init__(self, in_channels: int, out_channels: int, modes1: int, modes2: int):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.modes1 = modes1  # Number of Fourier modes to retain along height axis
        self.modes2 = modes2  # Number of Fourier modes to retain along width axis
        
        # Initialize complex parameters
        # Hint: Parameter of shape (in_channels, out_channels, modes1, modes2, dtype=torch.cfloat)
        raise NotImplementedError("Implement SpectralConv2d __init__.")

    def compl_mul2d(self, input_tensor: torch.Tensor, weights: torch.Tensor) -> torch.Tensor:
        """
        Multiply complex Fourier coefficients by complex weight matrices.
        Hint: Use torch.einsum.
        """
        raise NotImplementedError("Implement compl_mul2d.")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Input shape: (batch_size, in_channels, H, W)
        1. Compute 2D rfft
        2. Create output spectral tensor
        3. Multiply top-left and bottom-left spectrum corners using complex weights
        4. Compute 2D irfft back to physical space
        """
        raise NotImplementedError("Implement SpectralConv2d forward pass.")


class FNO2d(nn.Module):
    """
    2D Fourier Neural Operator (FNO) model.
    Appends coordinate grid, projects to higher width channels,
    performs spectral and local convolutions, and projects back to output fields.
    """
    def __init__(self, in_channels: int, out_channels: int, modes1: int, modes2: int, width: int):
        super().__init__()
        self.modes1 = modes1
        self.modes2 = modes2
        self.width = width
        
        # Define architecture: lifting, 4 spectral convs + 1x1 convs, projection layers
        raise NotImplementedError("Implement FNO2d __init__.")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Input shape: (batch_size, in_channels, H, W)
        Returns: predicted fields (batch_size, out_channels, H, W)
        """
        raise NotImplementedError("Implement FNO2d forward pass.")
