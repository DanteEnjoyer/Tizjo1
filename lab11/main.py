#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    #print(format_string)
    shouldDo = True
    i = 0
    counter = 0
    for idx in range(0,len(format_string)):
        if shouldDo:
            if i >= len(format_string):
                break
            if format_string[i] == '#':
                if format_string[i+1] != 'b':
                    print(format_string[i],end="")
                    i = i+1
                    continue
                result = ""
                param = int(param)
                binary = str(format(param, 'b'))[::-1]          
                for c in binary:
                    if c == '1':
                        if counter >= 10:
                            counter = 0
                        result += chr(ord(c) + 48 + counter)
                    else:
                        result += c
                    counter += 1
                print(result[::-1],end="")
                i = i+2
            else:
                print(format_string[i],end="")
                i = i+1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
