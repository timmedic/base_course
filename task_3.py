Year = int(input('Введите год: '))

if (Year % 4 == 0 and not Year % 100 == 0) or (Year % 100 and Year % 400):
    print('Високосный')
else:
    print('НЕ високосный')