#!/usr/bin/env python3
import sys

data = []

def off_by_one(a,b):
    s1 = set(a)
    s2 = set(b)
    diff=list(s1 ^ s2)
    if len(diff) == 2:
      print("{}  {}  {} ".format(diff, a, b, ))

for line in sys.stdin:
    data.append(line.rstrip("\n"))

data.sort()

for i in range(0,len(data)-1):
    j = i + 1
    off_by_one(data[i],data[j])

