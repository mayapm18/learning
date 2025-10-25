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
    """
    Three steps:
    1. Go through s and look for pair of equal consecutive characters
    2. If we find two equal consecutive characters - 
            2.1 remove them from s and create new_s
            2.2 return superReducedString(new_s) or 'Empty string' 
    3. Else:
        return s ?why?
    """    
    # Step 1
    has_two_equal = False
    new_s = ''
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            has_two_equal = True
            new_s = new_s + ''
            has_two_equal = False
        else:
            new_s = new_s + s[i]
    if has_two_equal:
        # step 2.2
        # TODO
        if new_s == '' :
            return 'Empty string'
        else:
            return superReducedString(new_s)
    else:
        # Step 3
        #TODO
        return s
            
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
