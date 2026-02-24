#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    val = arr[-1]
    done = 0
    
    j = -1
    for i in range(n-1, -1, -1):
        if i == n-1:
            continue
        if val < arr[i]:
            arr[j] = arr[i]
            j -= 1
        else:
            arr[j] = val
            print(*arr)
            done = 1
            break
    
        print(*arr)
    
    if not done:
        arr[0] = val
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)