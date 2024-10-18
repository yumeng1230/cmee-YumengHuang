#!/usr/bin/env python3

# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )

# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.
month_more_than_100mm=[i for i in rainfall if i[1] > 100]
print(month_more_than_100mm)
# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm. 
month_less_50mm=[i[0] for i in rainfall if i[1] < 50]
print(month_less_50mm)

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 
month_more_than_100mm=[]
for i in rainfall:
   if i[1] > 100:
      month_more_than_100mm.append(i)
print(month_more_than_100mm)

month_less_50mm=[]
for i in rainfall:
    if i[1] < 50:
        month_less_50mm.append(i[0])
print(month_less_50mm)

# A good example output is:
#
# Step #1:
# Months and rainfall values when the amount of rain was greater than 100mm:
# [('JAN', 111.4), ('FEB', 126.1), ('AUG', 140.2), ('NOV', 128.4), ('DEC', 142.2)]
# ... etc.

