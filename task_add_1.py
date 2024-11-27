import matplotlib.pyplot as plt
import numpy as np
import random

def lis():
    t = np.arange(-30, 30, 0.01)
    phase, A, a, B, b = np.pi / 2, 1, 1, random.randint(-10, 10), random.randint(0, 20)

    x = A * np.sin(a * t + phase)
    y = B * np.sin(b * t)

    plt.plot(x, y)

if(__name__ == '__main__'):
    lis()
    plt.savefig('task_add_1')