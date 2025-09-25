#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true

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

def result_cal(element, arr):
    R = 1
    for k in arr:
        if k == element:
            R = 0 
    return R
    
for p in arr_a:
    res = res + result_cal(p,arr_b)
for m in arr_b:
    res = res +result_cal(m,arr_a)

print(res)

        
