import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def CircleResize(time):
    alpha = np.arange(-2*np.pi, 2*np.pi, 0.1)
    R = 0.01 * time
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')

frames = 180
coords = np.zeros((frames, 2))

def Animate(i):
    ball.set_data(CircleResize(i))
    return ball

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, Animate, frames=frames, interval=30)
ani.save('task_2.gif', writer='pillow')