import math
import numpy as np

N = int(input("Введите число столбцов: "))
M = int(input("Введите число строк: "))

trigonometry_array = np.zeros((M, N))

for i in range(0, M-1, 1):
    for j in range(0, N-1, 1):
        trigonometry_array[i, j] = math.sin(N * i + M * j + 1)
        if(trigonometry_array[i, j] < 0):
            trigonometry_array[i, j] = 0
print(trigonometry_array)