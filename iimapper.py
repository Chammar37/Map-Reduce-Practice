#!/usr/bin/python3
import sys
import csv

# input = open("tester_2.txt", 'w')

data = csv.reader(sys.stdin)
next(data)

for line in data:  
    bus_information = line.split(",")
    categories_list = bus_information[len(bus_information)-1].split(';')

    for  category in categories_list:
        if '\r\n' in category:
             category = category.rstrip('\r\n')
        
        print(category + "\t" + bus_information[0])
        # input.write(category + "\t" + bus_information[0] + "\n")

# input.close()