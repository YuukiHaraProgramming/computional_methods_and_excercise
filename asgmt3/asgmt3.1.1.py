import numpy as np
from const1 import r0, v0, B, m, q, tau, f
from function.Euler_method import Euler_method
from function.ra31 import ra31
import matplotlib.pyplot as plt

def plt311_r(rx, ry):
    # 収束先を描画
    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(6, 6), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel='x', ylabel='y')
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)

    ax.scatter(rx, ry, label='r', s=2)
    ax.legend()
    plt.show()

def plt311_er(er):
    # 収束先を描画
    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(6, 6), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel='time', ylabel='er')
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)

    ax.scatter(np.arange(len(er)), er, label='er', s=2)
    ax.legend()
    plt.show()

def main():
    # 初期値の設定(Y=[r, v]とする)
    Y0 = np.array([r0, v0])
    h = tau / 64

    # Euler法で解く
    Y = Euler_method(f, Y0, h, tau)
    rx = np.array([])
    ry = np.array([])

    for i in range(len(Y)):
        el = Y[i]
        rx = np.append(rx, el[0][0])
        ry = np.append(ry, el[0][1])

    # 誤差を計算
    ra = ra31(h, tau)
    er = np.array([])
    for i in range(len(ra)):
        rc = np.array([rx[i], ry[i]])
        next_er = np.linalg.norm(rc - ra[i], ord=2)
        er = np.append(er, next_er)

    # 描画
    plt311_r(rx, ry)
    plt311_er(er)

if __name__ == '__main__':
    main()