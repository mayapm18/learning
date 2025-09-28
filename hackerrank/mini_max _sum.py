#https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_a = arr[0]
    max_a = arr[0]
    k = 0
    for a in arr:
        k = k + a  
        if a > max_a:
            max_a = a
        if a < min_a:
            min_a = a
    print(k - max_a,k - min_a)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
