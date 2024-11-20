import random
import time

constMaxTime = 15

def IsNumInList(num, list):
    for i in range(len(list)):
        if(num == list[i]):
            return True
    return False

n = int(input("Введите количество элементов: "))
array = []
[array.append(input(f"Введите элемент {i+1}: ")) for i in range(n)]
number = random.randint(0, n-1) + random.random()

startTime = time.time()
while(IsNumInList(number, array)):
    number = random.randint(0, n-1) + random.random()
    if(time.time() - startTime >= constMaxTime):
        print("Ошибка: превышено время ожидания")

if(not IsNumInList(number, array)):
    print(f"числа {number} нет в списке")