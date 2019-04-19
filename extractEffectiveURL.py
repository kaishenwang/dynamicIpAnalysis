import csv
import sys
import random
import string

alphabet = string.ascii_lowercase
for i in range(10):
    alphabet += str(i)

with  open(sys.argv[1]) as rawUrlFile, open('effectiveURL.txt', 'w') as effectiveURLFile, open('randSubURL.txt', 'w') as randSubURLFile:
    csv_reader = csv.reader(rawUrlFile, delimiter=',', quotechar='"')
    next(csv_reader, None)
    for row in csv_reader:
        if row[-1] == 'true':
            continue
        if row[0][:4] == 'http':
            effectiveURLFile.write(row[0] + '\n')
        else:
            effectiveURLFile.write('http:' + row[0] + '\n')
        randSubDomain = ''
        for i in range(5):
            randSubDomain += random.choice(alphabet)
        scheme = row[1]
        if len(scheme) == 0:
            scheme = 'http'
        randSubURLFile.write(scheme + '://' + randSubDomain + '.' + row[3] + '\n')
