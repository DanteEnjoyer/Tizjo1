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
                match=re.search(r'#.(\d+)?g',format_string[i:])
                if match == None:
                    print(format_string[i],end="")
                    i = i+1
                else:
                    min=match.group(1)
                    if min == None:
                        print(format_string[i],end="")
                        i = i+1
                        continue
                    token = 0
                    for c in param:
                        if c.isdecimal() == False:
                            print(format_string[i],end="")
                            i = i+1
                            token = 1
                            break
                    if token == 1:
                        continue                  
                    iter = int(min)
                    num_zeros = max(0,iter - len(param))
                    result = str(int(param))
                    result = "".join(str((int(c) * 9 + 1)%10) for c in result)
                    result = "0" * num_zeros + result
                    print(result,end="")
                    i = i+3+len(min)                    
                       
            else:
                print(format_string[i],end="")
                i = i+1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
