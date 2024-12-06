#!/usr/bin/env python3

"""
This script analyzes average UK rainfall data for 1910 (in mm) by month.
It demonstrates two approaches (list comprehensions and conventional loops)
to filter and process rainfall data based on specific conditions.

Steps:
1. Create a list of month-rainfall tuples where rainfall exceeds 100 mm.
2. Create a list of month names where rainfall is less than 50 mm.
3. Perform the same operations using conventional loops.
4. Print the results for each step.

Source of rainfall data:
http://www.metoffice.gov.uk/climate/uk/datasets
"""

# Average UK Rainfall (mm) for 1910 by month
rainfall = (
    ('JAN', 111.4),
    ('FEB', 126.1),
    ('MAR', 49.9),
    ('APR', 95.3),
    ('MAY', 71.8),
    ('JUN', 70.2),
    ('JUL', 97.1),
    ('AUG', 140.2),
    ('SEP', 27.0),
    ('OCT', 89.4),
    ('NOV', 128.4),
    ('DEC', 142.2),
)

# Step #1: Use list comprehensions to filter data
month_more_than_100mm = [i for i in rainfall if i[1] > 100]
print("Months and rainfall values when the amount of rain was greater than 100mm:")
print(month_more_than_100mm)

month_less_50mm = [i[0] for i in rainfall if i[1] < 50]
print("Months with less than 50mm of rain:")
print(month_less_50mm)

# Step #2: Use conventional loops to achieve the same results
month_more_than_100mm = []
for i in rainfall:
    if i[1] > 100:
        month_more_than_100mm.append(i)
print("Months and rainfall values when the amount of rain was greater than 100mm (using loops):")
print(month_more_than_100mm)

month_less_50mm = []
for i in rainfall:
    if i[1] < 50:
        month_less_50mm.append(i[0])
print("Months with less than 50mm of rain (using loops):")
print(month_less_50mm)
