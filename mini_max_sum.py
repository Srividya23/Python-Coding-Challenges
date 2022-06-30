# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# The function accepts INTEGER_ARRAY arr as parameter.

#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min_sum = 0
    max_sum = 0
    for i in range(0,len(arr)-1):
       min_sum = min_sum + arr[i]
    for j in range(1,len(arr)):
        max_sum = max_sum + arr[j]   
    print(min_sum,max_sum,sep=" ")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)