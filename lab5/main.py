#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    i=0
    for idx in range(0,len(format_string)):
        if shouldDo:
            if i>=len(format_string):
                break
            if format_string[i] == '#':
                match=re.search(r'#(\d+)?g',format_string[i:])
                if match == None:
                    print(format_string[i],end="")
                    i=i+1
                else:
                    min=match.group(1)
                    iter=int(min)
                    result = ""
                    for c in param:
                        if c == "0":
                            result+="9"
                        else:
                            result+=str(int(c)-1)  
                    if iter>len(param):
                        for z in range(iter-len(param)):
                            print(" ",end="")
                    print(result,end="")
                    i=i+2+len(min)                    
                       
            else:
                print(format_string[i],end="")
                i=i+1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
