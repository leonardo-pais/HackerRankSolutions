# Problem: https://www.hackerrank.com/challenges/staircase/problem

# Solution:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    empty = 0
    for i in range(1, n + 1):
        empty = n - i
        print(empty * ' ' + i * "#")

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
