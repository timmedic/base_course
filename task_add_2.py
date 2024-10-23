import numpy as np

length = int(input("Введите длина массива(< 10): "))
if(length > 10):
    print("Превышено кол-во ячеей. Будет создан массив размером в 10 ячеек")
    length = 10
arr = np.zeros((length))

for i in range(0, length, 1):
    arr[i] = input(f"{i}: ")
print(arr)

x = input("Введите содержимое новой ячейки: ")
n = int(input("Введите место новой ячейки: "))
newArr = np.zeros((length + 1))

for i in range(0, length + 1, 1):
    if(i < n-1):
        newArr[i] = arr[i]
    elif(i == n-1):
        newArr[i] = x
    else:
        newArr[i] = arr[i - 1]
print(newArr)