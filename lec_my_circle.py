import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(a=1, b=1, c=0):
    n = np.arange(-10, 10, 0.01)
    y = np.sin(n)
    x = np.cos(n)

    plt.plot(x, y, label='my circle')
    plt.axis('equal')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('circle plotter')
    plt.legend()
    plt.grid()

    plt.savefig('fig_3_1.png')

if(__name__ == '__main__'):
    circle_plotter()