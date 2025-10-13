#https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


# input translate:
# n=nums in a, m=nums in b
# arr_a
# arr_b


def find_lcm(x,y):
    if x>y:
        great = x
    else:
        great = y
        
    if great % x == 0 and great % y == 0:
        return great
    great = great + 1
    
            
def find_gcd(x,y):
    small = 0
    gcd_num = 1
    if x>y:
        small = y
    else:
        small = x 
        
    for k in range(small + 1):
        if x % k  == 0 and y % k == 0:
            gcd_num  = k
            
    return gcd_num 
    

def getTotalX(a, b):

    count = 0

    for p in range(len(a)):
        l = find_lcm(a[0], a[p])
    for k in range(len(b)):
        g = find_gcd(b[0], b[k])
    
    if l == g:
        count += 1
        
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
