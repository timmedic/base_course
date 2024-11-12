import math

def GetSquare(shape: str):
    if(shape == "circle"):
        R = float(input("Введите радиус окружности: "))
        return math.pi * (R ** 2)
    elif(shape == "rectangle"):
        a = float(input("Введите первую сторону прямоугольника: "))
        b = float(input("Введите вторую сторону прямоугольника: "))
        return a * b
    elif(shape == "triangle"):
        a = float(input("Введите первую сторону треугольника: "))
        b = float(input("Введите вторую сторону треугольника: "))
        c = float(input("Введите третью сторону треугольника: "))
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        print("Не удалось распознать фигуру")

print("Доступные фигуры - circle, rectangle, triangle")
shape = str(input("Выберите фигуру: "))
print(GetSquare(shape))