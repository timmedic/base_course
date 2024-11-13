import math

"""def GetSquare(shape: str):
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
print(GetSquare(shape))"""

def GetSquare(sizes: list):
    if(len(sizes) == 1):
        return math.pi * (sizes[0] ** 2)
    elif(len(sizes) == 2):
        return sizes[0] * sizes[1]
    elif(len(sizes) == 3):
        p = (sizes[0] + sizes[1] + sizes[2]) / 2
        return math.sqrt(p * (p - sizes[0]) * (p - sizes[1]) * (p - sizes[2]))
    else:
        print("Не удалось распознать фигуру")

def GetListOfInput():
    inputList = []
    symp = '0'
    print('Вводите размеры фигуры, которой площадь вы хотите найти. По завершению ввода, введите "*"')
    while(True):
        inputWord = input(">> ")
        if(inputWord == "*"):
            return inputList
        inputWord = float(inputWord)
        inputList.append(inputWord)

print(f"Площадь - {GetSquare(GetListOfInput())}")