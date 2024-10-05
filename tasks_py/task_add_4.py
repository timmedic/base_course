num = int(input('Введите число для разбивания на простые множители: '))
curr = 0

while(num != 1):
    if num % 2 == 0:
        num = num // 2
        curr = 2

    elif num % 3 == 0:
        num = num // 3
        curr = 3

    elif num % 5 == 0:
        num = num // 5
        curr = 5

    elif num % 7 == 0:
        num = num // 7
        curr = 7

    print(curr, end='')
    if num != 1:
        print('', end=' * ')
print('')