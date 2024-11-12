import numpy as np

def GetProd(array: list):
    product = 1
    for i in range(0, len(array)):
        product *= array[i]
    return product

size = int(input("Введите размер списка: "))
array = np.zeros((size))

for i in range(0, size):
    array[i] = int(input(f"Введите значение ячейки с номером {i + 1}: "))

print(f"Массив - {array}")
print(f"Произведение его членов - {GetProd(array)}")