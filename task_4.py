import numpy as np

def function(start, stop, n):
    x = start
    result = np.zeros((2, n))
    for i in range(0, n-1):
        result[0, n] = x
        result[1, n] = x ** 2
        x += ((stop - start) / n)
    return result

start = int(input("Выберите координату начала функции: "))
stop = int(input("Введите координату конца функции: "))
n = int(input("Введите число шагов: "))

print(function(start, stop, n))