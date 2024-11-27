import matplotlib.pyplot as plt
import numpy as np

def stairs(stairNum):
    x = []
    y = []
    for i in range(0, stairNum, 1):
        y.append(i)
        y.append(i+1)
        x.append(i)
        x.append(i)
    y.append(stairNum)
    x.append(stairNum)
    plt.plot(x, y)

if(__name__ == '__main__'):
    stairs(int(input('Введите количество ступенек: ')))
    plt.savefig('task_add_4.png')