def fibonacci(n):

    if n == 0:
        new_n = 0
        return new_n
    elif n == 1:
        new_n = 1
        return new_n
    else:
        new_n = (n - 1) + (n - 2)
        return fibonacci(new_n)
    

n = int(input())
print(fibonacci(n))