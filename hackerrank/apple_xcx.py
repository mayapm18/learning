#https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

#Input translate:
# s t
# a b
# m n
# apple dist
# orange dist


def countApplesAndOranges(s, t, a, b, apples, oranges):
    fall_a = 0
    fall_o = 0
    pos_a = []
    pos_o = []
    
    for x in apples:
        pos_a.append(a+x)

    for y in oranges:
        pos_o.append(b+y)
        
    for dis in pos_a:
        if dis <= t and dis >= s:
            fall_a = fall_a + 1
            
    for dist in pos_o:
        if dist <= t and dist >= s:
            fall_o = fall_o + 1
            
    print(fall_a)
    print(fall_o)
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
