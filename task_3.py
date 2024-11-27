import matplotlib.pyplot as plt
import plotter as pl
    

if(__name__ == '__main__'):
    dX = int(input('Введите предел изменения переменной x: '))
    N = int(input('Введите количество точек, разбивающий эллипс: '))
    pl.ellipse(0, 0, dX, 10, N)
    plt.axis('equal')
    plt.savefig('task_3.png')