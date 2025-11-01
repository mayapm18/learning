#https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#
def calc_maker(n, types, find):
    
    count = 0
    
    for i in types:
        for k in range(n):
            if find[k] == i:
                count = 1
    
    return count 
                
            
def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    finded = (calc_maker(n, numbers, password)+ calc_maker(n, lower_case, password)+ calc_maker(n, upper_case, password)+ calc_maker(n, special_characters, password))
    
    if n>=6:
        res = 4 - finded
        
    elif n == finded: #n = {1,2,3,4}
        res = 6 - n
        

    else: #n = {5} 
        if 6 - n <= 4 - finded: 
            res = 4 - finded
        else: # 6-n > 4 - finded 
            res = 6 - n 
    
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
