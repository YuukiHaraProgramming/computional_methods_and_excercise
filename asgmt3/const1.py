import numpy as np
from function.cross_product import cross_product3

r0 = np.array([-1, 0, 0])
v0 = np.array([0, 1, 0])

B = np.array([0, 0, 1])
m = 1
q = 1
tau = 2 * np.pi * m / (q * np.linalg.norm(B, ord=2))


# fの設定
def f(Y):
    dYdt = np.array([Y[1], q / m * cross_product3(Y[1], B)])
    return dYdt