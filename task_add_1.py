print('ax^2 + bx + c = 0')

a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

D = (b ** 2) - (4 * a * c)

if(D < 0):
    print('Нет корней')
elif(D == 0):
    x = b / (2 * a)
    print(f'Есть один корень: {x}')
else:
    x1 = ((D ** 0.5) - b) / (2 * a)
    x2 = ((D ** 0.5) + b) / (2 * a)
    print(f'Есть два корня: {x1} и {x2}')