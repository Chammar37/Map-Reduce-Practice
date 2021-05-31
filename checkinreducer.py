import sys
import re


previous = None
total = 0

output = open("checkinsbyday.txt", 'w')
for line in sys.stdin:
    key,value = line.split("#")

    if key != previous:
        if previous is not None:
            output.write( previous + ', #' + str(total) + '\n')
        previous=key
        total = 0
    
    total = total + int(value)


output.write(previous + ', #' + str(total) + '\n')
output.close()