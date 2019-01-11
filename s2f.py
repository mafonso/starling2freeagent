#!/usr/bin/env python3

import csv
import sys
import os

def convertCSV(filename):
    with open(filename, "rt") as source, open("fa-" + os.path.basename(filename), "wt") as result:
        rdr = csv.reader(source)
        wtr = csv.writer(result, delimiter=',', )
        next(rdr)  # Skip CSV headers
        next(rdr)  # Skip "Opening balance."
        for row in rdr:
            wtr.writerow([row[0], row[4], row[2]])

def main(argv):
    convertCSV(argv[0])

if __name__ == "__main__":
    main(sys.argv[1:])
