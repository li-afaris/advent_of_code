#!/usr/bin/env python3
import sys
data = sys.argv
data.pop(0)
frequency = 0

def calc_freq(total, arg ):

    if arg.startswith("+"):
        total = total  + int(arg.lstrip('-'))
    elif arg.startswith("-"):
        total = total  - int(arg.lstrip('-'))
    else:
        raise Exception("unknown operand")
    return total

for dp in data:
    try:
        frequency = calc_freq(frequency, dp)
    except Exception as e:
        print(e)
        sys.exit(1)

print("Frequency is: {}".format(frequency))