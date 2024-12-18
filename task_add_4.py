import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

x, y = [], []
fig, ax = plt.subplots()
animObject, = plt.plot([], [], color='k')

edge = 5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def GetSquare(x0=0, y0=0, dx=1, dy=1):
    xBufPoints = np.array([x0, x0+dx, x0+dx, x0, x0])
    yBufPoints = np.array([y0, y0, y0+dy, y0+dy, y0])
    return xBufPoints, yBufPoints

def RotateSquare(xPoints, yPoints, t):
    xRotPoints = t * np.cos(xPoints)
    yRotPoints = t * np.sin(yPoints)
    return xRotPoints, yRotPoints

def Update(i):
    coords = RotateSquare(x, y, i)
    animObject.set_data(coords[0], coords[1])

if(__name__ == '__main__'):
    x = GetSquare(-1, -1, 2, 2)[0]
    y = GetSquare(-1, -1, 2, 2)[1]
    ani = FuncAnimation(fig, Update, frames=np.arange(0, 360), interval=30)
    ani.save('task_add_4.gif', writer='pillow')