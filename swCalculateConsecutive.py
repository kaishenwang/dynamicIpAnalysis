import json
from os import listdir
from os.path import isfile, join
import copy
from operator import itemgetter
from collections import deque

folderPath = "/home/kwang40/alookupResult/"
deq = deque(maxlen=4)

def updateDeq(fileName):
    with open(fileName) as f:
        rr = f.readlines()
    deq.append(dict())
    for line in rr:
        data = json.loads(line)
        domain = data["name"]
        if data["status"] == "NOERROR":
            deq[-1][domain] = {}
            for ip in data["data"]["ipv4_addresses"]:
                deq[-1][domain][ip] = 1

files = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
files.sort()
domainIpDict = {}
domainChangeCount = {}
totalIpCount = 0

with open(join(folderPath, files[0])) as f:
    rr = f.readlines()
for line in rr:
    totalIpCount += 1
    data = json.loads(line)
    domain = data["name"]
    domainChangeCount[domain] = [0]*4


for i in range(3):
    updateDeq(join(folderPath, files[i]))

for i in range(3, min(5*24*3,len(files))):
    updateDeq(join(folderPath, files[i]))
    with open(join(folderPath, files[i])) as f:
        rr = f.readlines()
    newIpCount = 0
    disAppearIpCount = 0
    ipChangeCount = 0
    validIpCount = 0

    message = str(i)+","+str(i/3.0)+","
    message += str(validIpCount*100.0/totalIpCount)+","
    message += str(newIpCount*100.0/totalIpCount)+","
    message += str(disAppearIpCount*100.0/totalIpCount)+","
    message += str(ipChangeCount*100.0/totalIpCount)+","
    print (message)

sorted_list = sorted(domainChangeCount.items(), key=lambda x: x[1][0], reverse=True)
with open('changeDomainsSlidingWindow.txt', 'w') as fp:
    fp.write('\n'.join('%s %s' % x for x in sorted_list))
