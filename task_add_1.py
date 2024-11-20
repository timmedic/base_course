import random
import time
import numpy as np

def function(x):
    array[x] = (a * (x ** 4) + b * (x ** 3) + c * (c ** 2) + d * (x) + e)

a, b, c, d, e = random.randint(0, 20), random.randint(0, 20), random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)
numRange = range((10 ** 5 + 1))

array = list(numRange)
mapTime = time.time()
list(map(function, array))
mapTime = time.time() - mapTime

array = list(numRange)
listTime = time.time()
[function(num) for num in array]
listTime = time.time() - listTime

array = list(numRange)
forTime = time.time()
for i in array:
    function(i)
forTime = time.time() - forTime

print(f"Время map - {mapTime}")
print(f"Время спискового исключения - {listTime}")
print(f"Время цикла for - {forTime}")