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
    value = arr[-1]
    index = n-1
    while index > 0 and arr[index-1] > value:
        arr[index] = arr[index-1]
        print((" ").join(map(str, arr)))
        index -= 1
    arr[index] = value
    print((" ").join(map(str, arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
