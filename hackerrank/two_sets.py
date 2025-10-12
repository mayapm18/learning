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

#need: lcm_in_a, gcd_in_b
#x*lcm
#gcd/y
#how many lcm*x=gcd/y
def lcm_a_multiply(a):
    lcm_a = 0
    for k in a:
        if k>lcm_a:
            lcm_a = k
    print(lcm_a)
    #make arr with all the multiplying numbers with lcm
    # KUNY FIXED
          
            
def gcd_b_divide(b):
    gcd_b = 0
    for m in b: 
        if m< gcd_b:
            gcd_b = m
    print(gcd_b)
    #make arr for dividing gcd

def getTotalX(a, b):
    #lcm*x=gcd/y?
    # how many numbers are like that
    count = 0
    
    for x in lcm_a_multiply:
        for y in gcd_b_divide:
            if x == y:
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
