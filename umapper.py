#!/usr/bin/python3
import sys
import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk import ngrams
# nltk.download('punkt')

input = open("tester_2.txt", 'w')

for line in sys.stdin:
    line = re.sub('"', '', line)

    words = line.split(",")
    
    tokenizer = RegexpTokenizer("[\w']+")
    # # [\w']+

    comments = []
    comments.append(tokenizer.tokenize(words[0]))

    for words in comments:
        for word in words:
            input.write( word + "\t1" + "\n")
            # print(str(word) + "\t1")

input.close()