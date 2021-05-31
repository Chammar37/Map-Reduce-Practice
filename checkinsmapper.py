import sys
import re
import csv

#yelp_business, day, #checkins

test1= "hello1"
test2 = "test2"
test3 = 21

for checkins in sys.stdin.readlines()[1:]:
    #Split every column (column is represented by a comma ,) too look at them seperately and remove unwanted
    business_date = checkins.split(",")
    #Because we split every column by a , we can now remove the unwanted second/last column
    business_date.remove(business_date[2])

    #Now that second word is removed, we have less data filter through, saving time
    #Print what we want out for reference and reducer use

    print("%s, %s, #%d" % (business_date[0], business_date[1], int(business_date[2])))




