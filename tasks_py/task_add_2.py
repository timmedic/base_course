a = int(input('Введите первую сторону треугольника: '))
b = int(input('Введите вторую сторону треугольника: '))
c = int(input('Введите третью сторону треугольника: '))

if (a < b + c) and (b < a + c) and (c < a + b):
    print('Этот треугольник существует')
    if (a == b or a == c or b == c):
        if(a == b and b == c):
            print('Этот треугольник равносторонний')
        else:
            print('Этот треугольник равнобедренный')
    else:
        print('Этот треугольник разносторонний')
else:
    print('Этого треугольника НЕ существует')