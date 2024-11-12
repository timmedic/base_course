import numpy as np

def GetMiddle(array: list):
    middle = 0
    for i in range(0, len(array)):
        middle += array[i]
    return middle / len(array)

size = int(input("Введите размер списка: "))
array = np.zeros((size))

for i in range(0, size):
    array[i] = int(input(f"Введите значение ячейки с номером {i + 1}: "))
    
print(f"Массив - {array}")
print(f"Среднее значение - {GetMiddle(array)}")