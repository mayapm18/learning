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
    for type_b in range(6):
        for a in arr:
            if a == type_b:
                count[type_b] += 1
    return count

def migratoryBirds(arr):
    count_birds = find_the_same_bird(arr)
    max_bird = 0
    res_bird = 0
    
    for a in arr: 
        if count_birds[a] > max_bird:
            max_bird = count_birds[a]
            res_bird = a
        elif max_bird == count_birds[a]:
            #the smaller int(a) stay=res_bird
            if a < res_bird:
                res_bird = a
    
    return res_bird
            
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
