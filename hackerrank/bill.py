#https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#


def bonAppetit(bill, k, b):
    total = 0
    
    for a in bill:
        total += int(a)
    total = total - bill[k]
    if (total/2) == b:
        print('Bon Appetit') 
    elif b > (total/2):
        print (int(b - (total/2)))
    else:
        print(int((total/2) - b))
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
