import numpy as np

xLength = int(input("Введите число столбцов: "))
yLength = int(input("Введите число строк: "))

arr1 = np.zeros((yLength, xLength))
arr2 = np.zeros((yLength, xLength))
arrMax = np.zeros((yLength, xLength))

for y in range(0, yLength, 1):
    for x in range(0, xLength, 1):
        arr1[y, x] = int(input(f"1)[{x}, {y}]: "))

for y in range(0, yLength, 1):
    for x in range(0, xLength, 1):
        arr2[y, x] = int(input(f"2)[{x}, {y}]: "))

for y in range(0, yLength, 1):
    for x in range(0, xLength, 1):
        arrMax[y, x] = max(arr1[y, x], arr2[y, x])
print("array 1)", arr1, sep="\n")
print("array 2)", arr2, sep="\n")
print("array of max", arrMax, sep="\n")