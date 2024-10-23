import numpy as np

xLength = int(input("Введите число столбцов: "))
yLength = int(input("Введите число строк: "))

arr = np.zeros((yLength, xLength))

for y in range(0, yLength, 1):
    for x in range(0, xLength, 1):
        arr[y, x] = int(input(f"1)[{x}, {y}]: "))

print(arr)

for x in range(0, xLength, 1):
    print(f"{x + 1}) {max(arr[::,x])}")