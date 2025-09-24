#https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

count_a = int(input())
s1 = input()

count_b = int(input())
s2 =  input()

arr_a = []
arr_b = []

def make_arr(s):
    arr = []
    s = s + ' '
    k = ''
    for x in s:
        if x == ' ':
            arr.append(k)
            k = ''
        else:
            k = k + x
    return arr
              
arr_a = make_arr(s1)
arr_b = make_arr(s2)

res = 0
for a in arr_a:
    R = 1
    for b in arr_b:
        if a == b:
            R = 0 
    res = res + R
    
print(res)     
    
        