#!/usr/bin/env python3

import sys
import re
def my_printf(format_string,param):
    shouldDo=True
    i=0
    for idx in range(0,len(format_string)):
        if shouldDo:
            if i>=len(format_string):
               break
            if format_string[i] == '#':
                match = re.search(r'#([1-9]\d*)?(\.[1-9]\d*)?k',format_string[i:])
                if match == None:
                    print(format_string[i],end="")
                    i=i+1
                    continue
                min = match.group(1)
                max = match.group(2)
                if min == None and max == None:
                    print(param.swapcase(),end="")
                    i=i+2
                    continue
                if min == None and max != None:
                    iter=int(max[1:])
                    print(param[0:iter].swapcase(),end="")
                    i=i+2+len(max)
                    continue
                if min != None and max == None:
                    iter=int(min)
                    if iter>len(param):
                        for z in range(iter-len(param)):
                            print(" ",end="")
                    print(param.swapcase(),end="")
                    i=i+2+len(min)
                    continue
                if min != None and max != None:
                   iter=int(max[1:])
                   iter1=int(min)
                   if iter>len(param):
                       iter=len(param)
                   if iter1>iter:
                       for z in range(iter1-iter):
                           print(" ",end="")
                   print(param[0:iter].swapcase(),end="")
                   i=i+2+len(min)+len(max)
                   continue
            else:
                print(format_string[i],end="")
                i=i+1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
