import matplotlib.pyplot as plt
import numpy as np

def convertToDecart(alpha, r):
    return (r * np.cos(alpha), r * np.sin(alpha))

def Log(k):
    alpha = np.arange(0, 8 * np.pi, 0.01)
    r = np.pow(np.e, k * alpha)
    return(alpha, r)

def Arch(k):
    alpha = np.arange(0, 8 * np.pi, 0.01)
    r = k * alpha
    return(alpha, r)

def Rod(k):
    alpha = np.arange(0.01, 8 * np.pi, 0.01)
    r = k / np.sqrt(alpha)
    return(alpha, r)
def Rose(k):
    alpha = np.arange(0, 8 * np.pi, 0.01)
    r = np.sin(k * alpha)
    return(alpha, r)

def ChangeFunc():
    print('Доступны функции:\n1 - логарифмическая спираль\n2 - спираль Архимеда\n3 - спираль "Жезл"\n4 - роза')
    answer = int(input('Введите номер функции: '))
    k = float(input('Введите коэффицент: '))
    if(answer == 1):
        polar = Log(k)
    elif(answer == 2):
        polar = Arch(k)
    elif(answer == 3):
        polar = Rod(k)
    elif(answer == 4):
        polar = Rose(k)
    decart = convertToDecart(polar[0], polar[1])
    plt.plot(decart[0], decart[1])

if(__name__ == '__main__'):
    ChangeFunc()
    plt.axis('equal')
    plt.savefig('task_4.png')