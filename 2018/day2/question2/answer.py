#!/usr/bin/env python3
import sys

data = []
found = True

def off_by_one(a,b):
    print("{}   {}   {}   {}".format(a,b, list(set(a) ^ set(b)), "".join(list(set(a) & set(b)))))



for line in sys.stdin:
    data.append(line.rstrip("\n"))

data.sort()


while found:
    try:
        v1 = data.pop(0)
        v2 = data.pop(0)
        off_by_one(v1,v2)

    except IndexError:
        found = False
