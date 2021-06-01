#!/usr/bin/python3
import sys
import re

# input = open("tester_1.txt", 'w')

for line in sys.stdin:
    next(line)

    line = line.split(",")[0]
    line = re.sub(r'^\W+|\W+$', '', line)
    words = re.split(r'\W+', line)

    for word in words:
        # input.write( word.lower() + "\t1" + "\n")
        print(str(word.lower()) + "\t1")

# input.close()