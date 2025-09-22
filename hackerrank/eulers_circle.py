# https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

m = int(input())
s1 = input()

n = int(input())
s2 = input()

arr_1 = []
arr_2 = []
def conv_str_to_arr(s):
    arr=[]
    s=s+' '
    w = ''
    for x in s:
        if x == ' ':
            arr.append(w)
            w = ''
        else:
            w = w + x
    
    return arr
        
arr_1 = conv_str_to_arr(s1)
arr_2 = conv_str_to_arr(s2)

res = 0
def det_a_in_b(a, b):
    R = 1
    for x in b:
        if x == a:
            R = 0
            
    return R

for y in arr_1:
    res = res + det_a_in_b(y, arr_2)


            
print(res)


a = 2
b = [1,1,2,3,4,5]
def det_a_in_b(a, b):
    res = 1
    for x in b:
        if x == a:
            res = 0
            
    return res
            