#!/usr/bin/python3
import sys
import re
import csv

# input = open("tester_3.txt", 'w')

for line in csv.reader(sys.stdin):
    line = line.split(",")[0]
    line = re.sub(r'^\W+|\W+$', '', line)
    words = re.split(r'\W+', line)

    second_next = None
    third_next = None
    second_index = 1
    third_index = 2

    for index in range(len(words) - 2):
        # Next value
        second_next = words[second_index]
        third_next = words[third_index]

        # input.write(words[index].lower() + " " + second_next.lower() + " " + third_next.lower() + "\t1" + "\n")
        print(words[index].lower() + " " + second_next.lower() + " " + third_next.lower() + "\t1")
        # Increase index
        second_index += 1
        third_index += 1

# input.close()