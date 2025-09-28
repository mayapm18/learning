#http://hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max_of_a = candles[0]
    count_of_max = 0
    for a in candles:
        if a > max_of_a:
            max_of_a = a
            count_of_max = 1
        elif a == max_of_a:
            count_of_max += 1
            
    return count_of_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
