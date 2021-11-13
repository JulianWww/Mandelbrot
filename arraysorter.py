import numpy as np

# Defines the amount of rows & columns and the step size
rows = 100        # <---- CHANGE THIS
columns = 100     # <---- CHANGE THIS
step_size = 0.01  # <---- CHANGE THIS

# Does literally everything. It makes the entire array.
def arraymaker():
    arr = np.zeros((columns + 1, rows + 1), dtype=np.complex64)
    for i in range(0, rows + 1):
        for p in range(0, columns + 1):
            arr[i][p] = complex(i * step_size, p * step_size)
    return arr

if __name__ == '__main__':
    arr = arraymaker()
    print(arr)
