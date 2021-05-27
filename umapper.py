#!/usr/bin/python3
import sys
import re
from nltk.tokenize import RegexpTokenizer

# input = open("tester_1.txt", 'w')

for line in sys.stdin:
    line = re.sub('"', '', line)

    words = line.split(",")

    comments = []
    comments.append(words[0])

    tokenizer = RegexpTokenizer("[\w']+") 
    # [\w']+
    words = tokenizer.tokenize(comments[0])

    for word in words:
        # input.write( word.lower() + "\t1" + "\n")
        print(word.lower() + "\t1")

# input.close()