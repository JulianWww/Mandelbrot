import torch
import numpy as np
import time, warnings

warnings.filterwarnings('ignore')

device = torch.device("cpu")
if torch.has_cuda and torch.has_cudnn:
    device = torch.device("cuda")

def createBaseComplexImageMatrix(start_real, start_imag, end_real, end_imag, step):
    real, imag = torch.meshgrid(
        torch.arange(start_real, end_real+step, step, device=device),
        torch.arange(start_imag, end_imag+step, step, device=device)
        )
    return real + imag * complex(0,1)

def generatorStep(z, c, count):
    "return z^2+c"
    mask = torch.where(torch.abs(z) <= 2)
    z_masked = z[mask]
    c_masked = c[mask]
    z[mask] =  z_masked**2+c_masked
    count[mask] += 1
    return z

def generateSet(c, interations):
    "generate the set for values c for interations interations"
    z = torch.clone(c)
    count = torch.zeros_like(c, dtype=torch.int, device=device)
    for iteration in range(interations):
        z = generatorStep(z,c, count)
    return count.to(torch.device("cpu"))
    


t0 = time.time()
arr = createBaseComplexImageMatrix(-2,-2,2,2,0.001)
out = generateSet(arr, 100)
t1 = time.time()
print(t1-t0)
np.save("image.npy", out.cpu().numpy())


# 21.363631010055542
