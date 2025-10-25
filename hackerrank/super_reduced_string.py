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
    
def HelpRed(s):
    empty = ''
    skip = False
    for i in range(len(s) - 1):
        if skip:  # check if we need to skip this char
            skip = False  # reset skip
            continue

            
        if s[i] == s[i + 1]:
            skip = True  # skip the next char
        else:
            empty = empty + s[i]  
    return empty  
    
def superReducedString(s):
    empty = HelpRed(s)

    if empty == '':  
        return 'Empty String'
    else:
        return superReducedString(empty)  
                
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
