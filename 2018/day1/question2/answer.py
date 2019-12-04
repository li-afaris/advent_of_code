#!/usr/bin/env python3
import sys
from datetime import datetime

found = False
data = []
frequency = 0
loops = 0
duplicates = []
duplicates.append(frequency)

def calc_freq(total, arg ):
    if arg.startswith("+"):
        total = total  + int(arg.lstrip('-'))
    elif arg.startswith("-"):
        total = total  - int(arg.lstrip('-'))
    else:
        raise Exception("unknown operand")
    return total


for line in sys.stdin:
    data.append(line.rstrip("\n"))

while found == False:
    loops = loops + 1
    if loops % 100 == 0:
        print("{} loops = {} duplicates = {}".format(datetime.now().time(), loops, len(duplicates)))

    for value in data:
        frequency = calc_freq(frequency,value )
        if frequency in duplicates:
            print("Found duplicate: {}".format(frequency))
            print("Loop count {}".format(loops))
            sys.exit(0)
        duplicates.append(frequency)






