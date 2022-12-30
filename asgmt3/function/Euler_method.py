import numpy as np
from tqdm import tqdm

def Euler_method(f, Y0, h, tau):
    Y = np.array([Y0])
    for i in tqdm(range(int(tau / h))):
        next_Y = Y[i] + h * f(Y[i])
        Y = np.append(Y, next_Y).reshape(i+2, 2, 3)

    return Y