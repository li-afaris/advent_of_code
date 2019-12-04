#!/usr/bin/env python3

import sys


two_letter = {}
three_letter = {}

def  count_letters(name):
    namelist=list(name.lower())
    count = {}

    for letter in namelist:
       try:
                count[letter] = 1 + count[letter]
       except KeyError:
                count[letter] = 1

    for (k,v) in count.items():
        if v == 2:
            two_letter[name] = 1
        elif v == 3:
           three_letter[name] = 1




for line in sys.stdin:
    count_letters(line.rstrip("\n"))


checksum = len(two_letter.keys() ) * len(three_letter.keys())
print("Checksum: {}".format(checksum))