import sys
import re


#yelp_business, day, #checkins



for checkins in sys.stdin.readlines()[1:]:
    #Split every column (column is represented by a comma ,) too look at them seperately and remove unwanted
    business_date = checkins.split(",")
    #Because we split every column by a , we can now remove the unwanted second/last column
    business_date.remove(business_date[2])

    #Now that second word is removed, we have less data filter through, saving time
    #Print what we want out for reference and reducer use

    print("%s, %s, #%d" % (business_date[0], business_date[1], int(business_date[2])))




