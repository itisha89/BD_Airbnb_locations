#!/usr/bin/env python
"""reducer.py"""

import sys
from collections import defaultdict
from heapq import nlargest

# Dictionary to store the total count for each location
location_counts = defaultdict(float)

# Input comes from standard input (stdin)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Parse the input we got from mapper.py
    location, count = line.split('\t', 1)
    # Update the total count for the location
    location_counts[location] += float(count)

# Find the top 5 locations with the maximum number of counts
top_5_locations = nlargest(5, location_counts, key=location_counts.get)

# Print the top 5 locations with the maximum number of counts
print("Top 5 Locations with Maximum Number of Counts:")
for loc in top_5_locations:
    print(f"Location: {loc}, Number of Counts: {location_counts[loc]}")
