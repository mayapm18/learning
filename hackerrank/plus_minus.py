#https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for a in arr:
        if a > 0:
            pos = pos + 1
        elif a < 0:  #not working with if
            neg = neg + 1
        else:
            zero = zero + 1

    #f"{:.nf} -> n digits after the comma
    
    print(f"{pos / len(arr):.6f}")
    print(f"{neg / len(arr):.6f}")
    print(f"{zero / len(arr):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
