#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    
    start_arr = scores[0]
    min_score = 0
    max_score = 0
    
    for b in scores:
        if b < start_arr:
            start_arr = b
            min_score += 1
            
    for c in scores:
        if c > start_arr:
            start_arr = c
            max_score += 1
        
    
    
    return max_score, min_score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
