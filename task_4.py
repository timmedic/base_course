import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

x, y = [], []

def fillArray(n, x0, y0, C, D):
    x.append(x0)
    y.append(y0)
    for i in range(n):
        xn = x[len(x) - 1]
        yn = y[len(y) - 1]
        x.append( xn**2 - yn**2 + C)
        y.append( 2 * xn * yn + D)

fig, ax = plt.subplots()
animObject, = plt.plot([], [], color='b')

edge = 5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def Update(i):
    animObject.set_data(x[i], y[i])
    return animObject

if(__name__ == '__main__'):
    n, x0, y0, C, D = int(input('Введите число точек: ')), float(input('Введите x0: ')), float(input('Введите y0: ')), float(input('Введите C: ')), float(input('Введите D: '))
    fillArray(n, x0, y0, C, D)
