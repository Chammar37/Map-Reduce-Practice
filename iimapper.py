#!/usr/bin/python3
import sys
import re

input = open("tester_5.txt", 'w')

data = sys.stdin
next(data)

for line in data:

    # print((line[12]))

    categories = line.split(",")
    # busnies = category.split("'")
    

    # line = re.sub(r'^\W+|\W+$', '', line)
    # words = re.split(r'\W+', line)

    for category in categories:
        # cat = category.split(';')[13]
        input.write( str(category) + "\n")
        # print(str(word.lower()) + "\t1")

input.close()