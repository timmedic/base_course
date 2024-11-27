import matplotlib.pyplot as plt
import numpy as np

def convertToDecart(alpha, r):
    return (r * np.cos(alpha), r * np.sin(alpha))

def ellipse(p, e): 
    alpha = np.arange(0, 2 * np.pi, 0.01)
    r = p / (1 + e * np.cos(alpha))
    return(alpha, r)

if(__name__ == '__main__'):
    p = float(input('Введите фокальный параметр эллипса: '))
    e = float(input('Введите эксцентриситет эллипса: '))
    ellipse = ellipse(p, e)
    ellipseParams = convertToDecart(ellipse[0], ellipse[1])
    plt.plot(ellipseParams[0], ellipseParams[1])

    plt.axis('equal')
    plt.savefig('task_add_2.png')
