import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def Butterfly(t):
    x = np.sin(t) * (np.pow(np.e, np.cos(t)) - 2 * np.cos(4 * t) + np.pow(np.sin(t/12), 5))
    y = np.cos(t) * (np.pow(np.e, np.cos(t)) - 2 * np.cos(4 * t) + np.pow(np.sin(t/12), 5))
    return x, y

def Heart(t):
    x = 16 * np.pow(np.sin(t), 3)
    y = (13 * np.cos(t)) - (5 * np.cos(t*2)) - (2 * np.cos(t*3)) - np.cos(t*4)
    return x, y

x, y = [], []
fig, ax = plt.subplots()
animObject, = plt.plot([], [], color='g')

edge = 5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def UpdateButterfly(i):
    x.append(Butterfly(i)[0])
    y.append(Butterfly(i)[1])

    animObject.set_data(x, y)
    return animObject

def UpdateHeart(i):
    x.append(Heart(i)[0])
    y.append(Heart(i)[1])

    animObject.set_data(x, y)
    return animObject

if(__name__ == '__main__'):
    choice = int(input('0 - butterfly\n1 - not butter\n'))

    if(choice == 0):
        ani = FuncAnimation(fig, UpdateButterfly, frames=np.linspace(0, 12*np.pi, 1000), interval=30)
        ani.save('task_3_butterfly.gif', writer='pillow')
    elif(choice == 1):
        edge = 30
        ax.set_xlim(-edge, edge)
        ax.set_ylim(-edge, edge)
        ani = FuncAnimation(fig, UpdateHeart, frames=np.linspace(0, 2*np.pi, 100), interval=30)
        ani.save('task_3_heart.gif', writer='pillow')