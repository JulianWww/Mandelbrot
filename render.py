import numpy as np
import matplotlib.pyplot as plt

arr = np.load("image.npy")
plt.imshow(arr, cmap=plt.cm.binary)
plt.show()

