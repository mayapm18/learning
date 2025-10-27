def fibonacci(n):
    
    if(n<=1):
        return n
    f1 = 0
    f2 = 1
    for i in range(n): 
        new_f = f1+f2
        f1 = f2
        f2 = new_f
    return f1
    
n = int(input())
print(fibonacci(n))