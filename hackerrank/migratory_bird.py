#https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def find_the_same_bird(arr):
    count = 0
    for type_b in range(1, 6):
        for a in arr:
            if a == type_b:
                count[type_b] += 1
    return count


def migratoryBirds(arr):
    count_birds = find_the_same_bird(arr)
    max_bird = 0
    res_bird = 0
    
    for type_b in range(1, 6): 
        if count_birds[type_b] > max_bird:
            max_bird = count_birds[type_b]
            res_bird = type_b
        elif count_birds[type_b] == max_bird:
            if type_b < res_bird:
                res_bird = type_b
    
    return res_bird
        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
