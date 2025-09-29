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
def put_hms_in_arr(s):#ne maha poslednite '',''
    hms = ''
    arr = []
    for a in s:
        if a not in [':','P','A','M']:
            hms = hms + a
        else:
            arr.append(hms)
            hms = ''
    if hms == '':
        arr.append(hms)

    return arr #[hh, mm, ss]

def is_time_pm(s):
    for a in s:
        if a == 'P':
            return True
    return False
        

def fix_time(hh, mm, ss, is_pm):# TODO,  pm 0 do 11 stava +12, ako am 12 = 00
    
    
    if is_pm:
        hh = int(hh)
        if hh != 12:
            hh = hh + 12
        hh = str(hh)#==👇
        #     hh = str(hh)
        # else:
        #     hh = str(hh)
    else:
        print('hh=',hh)
        hh = int(hh)
        if hh == 12:
            hh = str(hh)
            hh='00'#int->str?
        else:
            if hh<10:
                hh = '0' + str(hh)
            else: 
                hh = str(hh)
    return hh, mm, ss
    
    
def timeConversion(s):
    
    arr = put_hms_in_arr(s)
    print('arr=', arr)
    hh = arr[0]
    mm = arr[1]
    ss = arr[2]

    is_pm = is_time_pm(s) # TODO
    print('is_pm=',is_pm)

    hh, mm, ss = fix_time(hh,mm,ss, is_pm) 
    
    
    return hh+':'+mm+':'+ss
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()