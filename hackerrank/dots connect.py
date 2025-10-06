#https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):   
    many_socks = 0 

    for a in range(n):
        if ar[a] == -1: #skip if ==ar[b]
            continue
        count = 1
        for b in range(a+1, n):
            if ar[a] == ar[b]:
                count = count + 1
                ar[b] = -1 #remove
                
        many_socks = many_socks + count//2
        ar[a] = -1
                
    return many_socks
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()