# Given a time in 12-hour AM/PM format, the function converts it to military (24-hour) time.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

# Note: 
#12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock
# 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#Example
#s='12:01:00PM' Returns '12:01:00'.
#s='12:01:00AM' Returns '00:01:00'.

#!/bin/python3

import math
import os
import random
import re
import sys



def timeConversion(s):
    # Write your code here
    s_hour = int(s[0:2])
    if(s.endswith("PM")):
        if(s_hour == 12):
            s_hour = 12
        else:
            s_hour = 12 + s_hour
        return(str(s_hour)+s[2:8])
    else:
        if(s_hour == 12):
            return("00"+s[2:8])
        else:
            return(s[0:8])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
