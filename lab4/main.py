#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    result=""
    result2=""
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'g':
                shouldDo=False
                if param == "":
                   continue
                flag_l = False
                for i in param:
                    if i.isalpha():
                        flag_l = True
                if flag_l == True:
                    continue
                result2+=str(int(eval(param)))
                result+= str(result2[::-1])
                result=str(int(result))
                print(result,end="")
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
