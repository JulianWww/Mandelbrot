import numpy as np

def createBaseComplexImageMatrix(start_real, start_imag, end_real, end_imag, step):
    "creates a 2d array of comples numbers using the start, end and step like np.arange"
    real, imag = np.meshgrid(
        np.arange(start_real, end_real+step, step),
        np.arange(start_imag, end_imag+step, step))
    return real + imag * complex(0,1)


print(createBaseComplexImageMatrix(-1,-1,1,1,1))
