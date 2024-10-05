start = 0
count = int(input('число элементов ряда Фибоначчи: '))

fib = []

for i in range(start, start + count + 1, 1):
    if len(fib) == 0:
        fib.append(i+1)
    elif len(fib) < 2:
        fib.append(fib[i-1])
    else:
        fib.append(fib[i-1] + fib[i-2])
    print(fib[i])