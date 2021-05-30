#!/usr/bin/python3
import sys
import re
from nltk.tokenize import RegexpTokenizer

# input = open("tester_3.txt", 'w')

for line in sys.stdin:
    line = re.sub('"', '', line)

    words = line.split(",")
    
    tokenizer = RegexpTokenizer("[\w']+")
    # # [\w']+

    comments = []
    comments.append(tokenizer.tokenize(words[0]))

    for words in comments:
        for word in words:
            # input.write( word.lower() + "\t1" + "\n")
            print(str(word.lower()) + "\t1")

# input.close()