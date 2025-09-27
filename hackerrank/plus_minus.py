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
        if a < 0: 
            neg = neg + 1
        else:
            zero = zero + 1
    
    print(pos / len(arr))
    print(neg / len(arr))
    print(zero / len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
