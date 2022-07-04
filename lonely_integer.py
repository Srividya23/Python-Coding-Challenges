# Given an array of integers, where all elements but one occur twice, the function finds the unique element.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.

#Example
# a = [1,2,3,4,3,2,1]. The unique element is 4.

#!/bin/python3

import math
import os
import random
import re
import sys

def lonelyinteger(a):
    # Write your code here
    for i in range(0,len(a)):
        count_num = a.count(a[i])
        if count_num==1:
            print(a[i],end="\n")
            return a[i]
            
        
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    #fptr.write(str(result) + '\n')

    #fptr.close()
