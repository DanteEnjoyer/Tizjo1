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
                match=re.search(r'#.(\d+)?j',format_string[i:])
                if match == None:
                    print(format_string[i],end="")
                    i = i+1
                else:
                    min=match.group(1)
                    if min == None:
                        print(format_string[i],end="")
                        i = i+1
                        continue   
                    if not param.isnumeric():
                        print(format_string[i],end="")
                        i = i+1
                        continue
                    new_res = ""        
                    temp = str(hex(int(param)))[2:]        
                    for c in temp:
                        if c in "abcdef":
                            new_res += chr(ord(c)+6)
                        elif c in "0":
                            new_res += "o"
                        else:
                            new_res += c                                                   
                    iter = int(min)
                    num_zeros = max(0,iter - len(new_res))
                    result = "o" * num_zeros + new_res
                    print(result,end="")
                    i = i+3+len(min)                    
                       
            else:
                print(format_string[i],end="")
                i = i+1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
