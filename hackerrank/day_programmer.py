#https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    if year < 1918:
        if year%4 == 0:
            return '12.09.' + str(year)
        else: 
            return '13.09.' + str(year)
    elif year == 1918:
        return '26.09.' + str(year)
    else: #year>1918
        if year%4 == 0: 
            if year%400 == 0: 
                return '12.09.' + str(year) 
            else: 
                if year%100 == 0: 
                    return '13.09.' + str(year) 
                else: 
                    return '12.09.' + str(year) 
        else: 
            return '13.09.' + str(year)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
