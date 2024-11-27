import matplotlib.pyplot as plt
import numpy as np

def gyperbola(dX=5, N=1):
    xm = np.arange(dX * (-1), -0.01, dX / N)
    xp = np.arange(0.01, dX, dX / N)
    ym = 0.5/xm
    yp = 0.5/xp

    plt.plot(xm, ym)
    plt.plot(xp, yp)
    plt.savefig('task_2.png')

if(__name__ == '__main__'):
    dX = int(input('Введите предел изменения переменной x: '))
    N = float(input('Введите количество точек, разбивающий гиперболу: '))
    gyperbola(dX, N)