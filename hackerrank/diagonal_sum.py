#https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum_pr=0
    sum_sec=0
    n=len(arr)
    result = 0
    
    for a in range(n):
        sum_pr += arr[a][a]
        sum_sec += arr[a][n-a-1]
    
    if sum_pr > sum_sec:
        result = sum_pr - sum_sec
    elif sum_pr == sum_sec:
        result = 0
    else:
        result = sum_sec - sum_pr

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
