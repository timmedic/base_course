import matplotlib.pyplot as plt
import numpy as np

def piece(a, b):
    x = np.arange(a - 10, b + 10, 1)
    y = np.arange(a - 10, b + 10, 1)
    for i in x:
        if(x[i] < a):
            y[i] = a ** 2
        elif(x[i] >= a and x[i] <= b):
            y[i] = x[i] ** 2
        elif(x[i] > b):
            y[i] = b ** 2
    
    plt.plot(x, y)

if(__name__ == '__main__'):
    piece(int(input('Введите a: ')), int(input('Введите b: ')) )
    
    plt.savefig('task_add_3.png')