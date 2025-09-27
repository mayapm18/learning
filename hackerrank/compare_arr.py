#https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    alice = 0
    bob = 0
    for k in range(len(a)):   
        if a[k]>b[k]:
            alice = alice + 1
        if a[k]<b[k]:
            bob = bob + 1
        else: 
            continue
                
    return [alice, bob]
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
