import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def CircleMove(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 2*np.pi, 0.25)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')

def Animate(i):
    ball.set_data(CircleMove(R=0.5, vx0=0.01, vy0=0.01, time=i))

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, Animate, frames=100, interval=30)
ani.save('animation_3.gif', writer='pillow')