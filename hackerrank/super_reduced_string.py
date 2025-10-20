#https://www.hackerrank.com/challenges/reduced-string/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    empty = ''
    for i in range(len(s)):
        if s[i] != s[i+1]:
            empty = empty 
            for j in range(len(s)):
                if j != i and j != i + 1:
                    empty = empty + s[j]
        else:
            empty = empty + s[i]
            
            
    return empty

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
