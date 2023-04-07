#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    count = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                is_sorted = False
                count += 1
                a[i], a[i+1] = a[i+1], a[i]
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
