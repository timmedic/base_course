import constans as const

def GetEnergy(m, h, V):
    return ((m * const.g * h) + ((m * (V ** 2)) / 2))

#mass = float(input("Введите массу тела(кг): "))
#height = float(input("Введите высоту, на которую тело поднялось(м): "))
#Velocity = float(input("Введите скорость тела(м/с): "))

#print(GetEnergy(mass, height, Velocity))

#вариант с меньшим использованием памяти
print(GetEnergy(  float(input("Введите массу тела:(кг)" ))  ,  float(input("Введите высоту, на которую тело поднялось(м): "))  ,  float(input("Введите скорость тела(м/с): "))  ))