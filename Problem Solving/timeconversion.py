#!/bin/python3

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

def timeConversion(s):
    # Write your code here
    hours = s[0:2]
    if s[8] == 'P' and hours != '12':
        hours = int(hours) + 12
        s = str(hours) + s[2:8]
    elif s[8] == 'P' and hours == '12':
        s = s[0:8]
    elif s[8] == 'A' and hours != '12':
        s = s[0:8]
    else:
        hours = '00'
        s = hours + s[2:8]
    return(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
