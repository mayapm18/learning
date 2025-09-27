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
    min_num = arr[0]
    max_num = arr[0]
    s = 0
    
    for a in arr: 
        s = s + a
        if a < min_num:
            min_num = a
        if a > max_num:
            max_num = a
            
    print(s-max_num, s-min_num)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
