import numpy as np
import phys_consts as pc
import random

x0 = random.randint(0, 100)
y0 = random.randint(0, 100)
v0 = random.randint(0, 100)

table = np.zeros((3, 6))

for t in range(0, 6, 1):
    table[0, t] = t
    table[1, t] = x0 + v0 * t
    table[2, t] = y0 + v0 * t - ((pc.g * (t ** 2)) / 2)
    print(f"time) {t}", f"x) {table[1, t]}", f"y) {table[2, t]}", sep="\n")