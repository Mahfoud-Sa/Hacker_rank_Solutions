#https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
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
    time_pre=s[-2:]
    time=s[:-2].split(':')
    
    # if the time is midnight
    if( time_pre=='AM' and int(time[0])==12):
        return "0{}:{}:{}".format(0,time[1],time[2])
    elif (time_pre =='PM' and time[0]=='12'):
       return s[:-2]
       
    elif (time_pre =='PM' and int(time[0])>=1):
       
        return "{}:{}:{}".format(int(time[0])+12,time[1],time[2])
    else:
         return s[:-2]



    

print(timeConversion('1:05:45AM'))