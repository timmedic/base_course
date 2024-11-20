import matplotlib.pyplot as plt
import numpy as np

def ellipse(dX=5, N=1):
    dY = 5
    x = np.arange(-dX, dX+1, 0.1)
    y = np.arange(-dY, dY+1, 0.1)

    X, Y = np.meshgrid(x, y )

    fxy = (X**2)/(2**2) + (Y**2)/(1**2)

    plt.contour(X, Y, fxy, levels=[1])
    plt.axis('equal')

    plt.savefig('task_3.png')

if(__name__ == '__main__'):
    dX = int(input('Введите предел изменения переменной x: '))
    N = int(input('Введите количество точек, разбивающий эллипс: '))
    ellipse(dX, N)