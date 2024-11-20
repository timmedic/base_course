import matplotlib.pyplot as plt
import numpy as np

def parabola(dX=5, N=1):
    x = np.arange(-dX, dX+1, (dX*2) / N)
    y = x**2

    plt.plot(x, y)
    plt.savefig('task_2.png')

if(__name__ == '__main__'):
    dX = int(input('Введите предел изменения переменной x: '))
    N = int(input('Введите количество точек, разбивающий параболу: '))
    parabola(dX, N)