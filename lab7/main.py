#!/usr/bin/env python3

import sys


def my_printf(format_string,param):
    #print(format_string)
    shouldDo = True
    i = 0
    for idx in range(0,len(format_string)):
        if shouldDo:
            if i >= len(format_string):
                break
            if format_string[i] == '#' and format_string[i+1] == 'j':

                i = i+2       
            else:
                print(format_string[i],end="")
                i = i+1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
