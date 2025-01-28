#!/usr/bin/env python3
"""mapper.py"""


import sys
import csv

# Input comes from standard input (stdin)
for line in sys.stdin:
    # Create a CSV reader object
    reader = csv.reader([line])
    # Read the row
    for row in reader:
        # Extract location name and review score
        location = row[0]
        score = float(row[1])  # Assuming the score is the second column
        # Emit the location as the key and the score as the value
        print('%s\t%s' % (location, score))

