import csv
import sys

with open('effectiveURL.txt', 'w') as effectiveURLFile:
    with open(sys.argv[1]) as rawUrlFile:
        csv_reader = csv.reader(rawUrlFile, delimiter=',', quotechar='"')
        for row in csv_reader:
            if row['IsIP'] == 'true':
                continue
            if row['URL'][:4] == 'http':
                effectiveURLFile.write(row['URL'] + '\n')
            else:
                effectiveURLFile.write('http:' + row['URL'] + '\n')
