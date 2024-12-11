import matplotlib.pyplot as plt
import numpy as np

def Cycloid(R = 3):
    t = np.arange(0, 10, 0.1)
    x = R * (t - np.pow(np.sin(t), 1))
    y = R * (1 - np.pow(np.cos(t), 1))

    plt.plot(x, y)
    plt.savefig('task_1_cycloid.png')

def Asteroid(R = 3):
    t = np.arange(0, 10, 0.1)
    x = R * np.cos(t) ** 3
    y = R * np.sin(t) ** 3

    plt.plot(x, y)
    plt.savefig('task_1_asteroid.png')

if(__name__ == '__main__'):
    plt.axis('equal')

    choice = int(input("1 - циклоида, 2 - астероида: "))

    if(choice == 1):
        Cycloid()
    elif(choice == 2):
        Asteroid()
    else:
        print('ERROR 404')