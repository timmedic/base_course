num = int(input('Введите число до которого все числа должны быть проверены на совершенность/несовершенность: '))

for curr in range(2, num+1, 1):
    sum = 0
    for i in range(1, curr, 1):
        if curr % i == 0:
            sum += i
    if curr == sum:
        print(curr)