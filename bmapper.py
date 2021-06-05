#!/usr/bin/python3
import sys
import re
import csv

# input = open("tester_2.txt", 'w')

for line in csv.reader(sys.stdin):
    line = line.split(",")[0]
    line = re.sub(r'^\W+|\W+$', '', line)
    words = re.split(r'\W+', line)

    next = None
    next_index = 1

    for index in range(len(words) - 1):
        # Next value
        next = words[next_index]

        # input.write( words[index].lower() + " " + next.lower() + "\t1" + "\n")
        print(words[index].lower() + " " + next.lower() + "\t1")
        # Increase index
        next_index += 1

# input.close()