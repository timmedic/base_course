def fib(n):
    first = 0
    second = 1
    if(n < 0):
        second = 1
    if(n == 0):
        return None
    elif(n == 1 or n == -1):
        return first
    elif(n == 2 or n == -2):
        return second
    else:
        for i in range(0, abs(n) - 1):
            first, second = second, first
            second += first
    if(num >= 0): 
        return second
    else:
        return -second

num = int(input("Введите номер числа фиббоначи: "))
print(fib(num))