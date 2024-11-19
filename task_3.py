import time
import random

startTime = time.time()

M = random.randint(0, 100)
N = random.randint(0, 100)

for i in range(0, M):
    for j in range(0, N):
        print(N, end="_")
    print(M)

print(time.time() - startTime)