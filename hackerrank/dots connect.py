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
    many_socks = int(n)//2 - 1
    print(many_socks)
    
    for a in range(n):
        for b in range(a+1, n):
            if ar[a]== ar[b]:
                ar[a] = -1 #mark as used
                ar[b] = -1 #mark as used
                break

                  
    return many_socks
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()