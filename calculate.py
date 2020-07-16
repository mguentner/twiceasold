#!/usr/bin/env python3
import datetime
import sys

if len(sys.argv) != 3:
    print("supply two dates")
    sys.exit(1)

dates = [ datetime.date.fromisoformat(sys.argv[1]), datetime.date.fromisoformat(sys.argv[2]) ]
dates.sort()
older = dates[0]
younger = dates[1]

d = abs(younger-older).days
x = 2*d
y = older + datetime.timedelta(days=x)
print("{} will be twice as old as {} on {}".format(older, younger, y))
