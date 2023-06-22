# Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true

# Solution:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    mini = arr[0]
    maxi = arr[0]
    soma_min = 0
    soma_max = 0
    for i in arr:
        if i < mini:
            mini = i
        elif i > maxi:
            maxi = i
        soma_max = soma_max + i
        soma_min = soma_min + i
    soma_max = soma_max - mini
    soma_min = soma_min - maxi
    print(soma_min, soma_max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
