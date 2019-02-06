import sys
import time
from datetime import datetime, timedelta


#python takeFrequentChangeDomain.py changeDomains.txt topCount(100) running time in mins (10)
with open(sys.argv[1]) as f:
    data = f.readlines()

domains = []
for i in range(min(len(data), int(sys.argv[2]))):
    domains.append(data[i].split(' ')[0])

endTime = datetime.now() + timedelta(minutes=int(sys.argv[3]))

while (datetime.now() < endTime):
    for domain in domains:
        print(domain)
    time.sleep(5)
