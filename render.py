import torch
import matplotlib.pyplot as plt

arr = torch.load("image.pt")
plt.imshow(arr, cmap=plt.cm.binary)
plt.show()

