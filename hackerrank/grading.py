#https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    arr = []
    
    for grade in grades:
        if grade > 38:
            for a in range(3):
                if (grade + a) % 5 == 0:
                    grade = grade + a
                else:
                    grade = grade
        else:
            grade = grade
    arr.append(grade)
    
    return arr
    
# Sample Input 0

# 4
# 73
# 67
# 38
# 33
# Sample Output 0

# 75
# 67
# 40
# 33
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
