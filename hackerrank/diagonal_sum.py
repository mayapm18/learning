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
    pr = 0
    sec = 0
    k= 0
    for a in range(len(arr)):
        pr = pr + arr[a][a]
        sec = sec + arr[a][len(arr)-a-1]
        
    if pr > sec:
        k = pr - sec
    if pr == sec:
        k = 0
    else:
        k = sec - pr
    return k


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
