import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
animObject, = plt.plot([], [], 'o', color='k')

edge = 5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def Cycloid(R = 3, t=0, isStatic=True):
    if(isStatic):
        t = np.arange(0, 10, 0.1)

    x = R * (t - np.pow(np.sin(t), 1))
    y = R * (1 - np.pow(np.cos(t), 1))

    if(isStatic):
        plt.plot(x, y)

    return x, y

def Asteroid(R = 3, t = 0, isStatic = True):
    if(isStatic):
        t = np.arange(0, 10, 0.1)

    x = R * np.cos(t) ** 3
    y = R * np.sin(t) ** 3

    if(isStatic):
        plt.plot(x, y)
    return x, y

def UpdateCycloid(i):
    coords = Cycloid(3, i, False)
    animObject.set_data(coords[0], coords[1])

if(__name__ == '__main__'):
    plt.axis('equal')

    choice = int(input("1 - циклоида, 2 - астероида: "))

    if(choice == 1):
        Cycloid()
        ani = FuncAnimation(fig, UpdateCycloid, frames=np.arange(0, 50), interval=30)
        ani.save('task_add_1.gif', writer='pillow')
    elif(choice == 2):
        Asteroid()
    else:
        print('ERROR 404')