#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    #print(format_string)
    shouldDo = True
    i = 0
    for idx in range(0,len(format_string)):
        if shouldDo:
            if i >= len(format_string):
                break
            if format_string[i] == '#':
                match = re.search("#\.(\d+)h",format_string[i:])
                if match == None:
                    print(format_string[i],end="")
                    i = i+1
                else:
                    min = match.group(1)
                    if min == None:
                        print(format_string[i],end="")
                        i = i+1
                        continue
                    param = float(param)
                    replace_with = f"{param:.{min}f}"               
                    first_part = ''
                    second_part = ''
                    if '.' in replace_with:
                        first_part, second_part = replace_with.split('.')
                    else:
                        first_part = replace_with
                    new_res = ''
                    for c in first_part:
                        if c in "0123456789":
                            new_res += chr(ord(c)+49)
                    new_res2 = ''
                    for m in second_part:
                        if m in "0123456789":
                            new_res2 += str((int(m)+5)%10)
                    result = new_res + ('.' if second_part else '') + new_res2    
                    print(result,end="")
                    i = i+3+len(min)                    
            else:
                print(format_string[i],end="")
                i = i+1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
