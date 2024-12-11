import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2)

x, y = [], []
parameter = np.linspace(0, 2*np.pi, 100)

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)

def Update(frame):
    x.append(frame)
    y.append(np.sin(frame))

    anim_object.set_data(x, y)

    return anim_object

ani = FuncAnimation(fig, Update, frames=parameter, interval=50)

ani.save('animation_1.gif', writer='pillow')