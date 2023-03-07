#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    shouldDo=True
    doNot=0
    for idx in range(0,len(format_string)):
        if shouldDo:
            doNot=doNot-1
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                print(param.swapcase(),end="")
                shouldDo=False
            elif format_string[idx] == '#' and format_string[idx+1] == '.': 
            	a=format_string.find('k',idx)
            	if a==-1:
            	    continue
            	b=int(format_string[idx+2:a])
            	doNot=a-idx+1
            	if b<0:
            	    continue
            	print(param[0:b].swapcase(),end="")
            else:
            	if doNot<=0:
                    print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
