#https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def put_hms_in_arr(s):
    hms = ''
    len(s) == len(s) - 2
    arr = []
    for a in s:
        if a != ':':
            hms = hms + a
        else:
            arr.append(hms)
            hms = ''
            
    #remove AM/PM
    arr.append(hms)  
    return arr


def timeConversion(s):
    arr = put_hms_in_arr(s)
    hh = arr[0]
    mm = arr[1]
    ss = arr[2]
    
    is_pm = False
    
    for x in s:    
            
        if x == 'P':
            is_pm = True
        
        if is_pm:
            if arr[0] == 12:
                hh = '00'
            else:
                hh = hh + 12
    print(hh,':', mm, ':', ss) 
            
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
#timeConversion(s)#
    result = put_hms_in_arr(s)

    fptr.write(result + '\n')

    fptr.close()
