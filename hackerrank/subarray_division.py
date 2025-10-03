#https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

#input translate
#how many nums in the chocolate
#chocolate
#sum=d , count of blocks to sum=m 
def birthday(s, d, m):
    win_choc = 0
    sum_of_a = 0
    
    for a in range(len(s) - m + 1):
        for b in range(m):
            sum_of_a = sum_of_a + s[a+b]
        if sum_of_a == d:
            win_choc = win_choc + 1
                
    
    return win_choc
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
