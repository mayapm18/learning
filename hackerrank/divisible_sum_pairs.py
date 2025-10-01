#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    curr_sum = 0
    count = -1
    
    for a in range(len(ar)):
        for b in range(len(ar) - 1 ):
                curr_sum = ar[a] + ar[b]
                if curr_sum == k:
                    count = count + 1
                    
    return count
                    
                
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
