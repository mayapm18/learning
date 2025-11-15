#https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem

def fibonacci(n):

    if n == 0:
        new_n = 0
        return new_n
    elif n == 1:
        new_n = 1
        return new_n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

n = int(input())
print(fibonacci(n))