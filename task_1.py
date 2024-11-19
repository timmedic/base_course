import numpy as np
import random

def FillArrayByRandom(array: np.array):
    for i in range(len(array)):
        array[i] = random.randint(0, 100)
    return array

N = int(input("Введите размер массивов: "))
arrays = [np.zeros((N)), np.zeros((N)), np.zeros((N))]

print(list(map(FillArrayByRandom, arrays)))
print("Большие значения в каждом из списков:" , list(map(max, arrays)))
print("Суммы всех значений каждого из списков:", list(map(sum, arrays)))