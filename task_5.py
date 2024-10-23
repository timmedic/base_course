from task_4 import trigonometry_array as ta
from task_4 import M as length

N1 = int(input("Какой столбец поменять: "))
N2 = int(input("На какой столбец поменять: "))

buffer = 0

print("Меняю столбцы...")

for i in range(0, length-1, 1):
    buffer = ta[i, N1-1]
    ta[i, N1-1] = ta[i, N2-1]
    ta[i, N2-1] = buffer

print(ta)