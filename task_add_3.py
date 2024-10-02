num = input('Введите число для переворачивания: ')
count = len(num)
num = int(num)

for i in range(1, count+1, 1):
    print((num % (10 ** i) // (10 ** (i-1))), end = '')