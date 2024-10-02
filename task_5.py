a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if (b == 0):
    print('ERROR: subdividing by zero')
elif(a % b == 0):
    print('Первое число делится нацело на второе')
else:
    print('Первое число НЕ делится нацело на второе')
    print(f'Остаток: {a % b}')

print(f'Частное - {a / b}')