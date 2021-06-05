#!/usr/bin/python3
import sys

previous_key = None
bus_ids = []
# categories_set = {'categories'} 

# input = open("inverted-index.txt", 'w')

for line in sys.stdin:
    key,value =  line.split( '\t' )

    if ('\n' in value):
        value = value.strip('\n')

    if key != previous_key:
        if previous_key is not None:
            print(previous_key + " " + ", ".join(bus_ids))

            bus_ids.clear()
            bus_ids.append(value)
        previous_key = key
    
    if (key == previous_key and value not in bus_ids):
        bus_ids.append(value)

# input.close()
