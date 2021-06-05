#!/usr/bin/python
import sys
import re
import csv

# input = open("tester_1.txt", 'w')

data = csv.reader(sys.stdin)
next(data)

for line in data:
    line = line.split(",")[0]
    line = re.sub(r'^\W+|\W+$', '', line)
    words = re.split(r'\W+', line)

    for word in words:
        # input.write( word.lower() + "\t1" + "\n")
        print(str(word.lower()) + "\t1")

# input.close()