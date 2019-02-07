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
        deq[-1][domain] = {}
        if data["status"] == "NOERROR":
            # record first ip
            deq[-1][domain]["0"] = data["data"]["ipv4_addresses"][0]
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
    newIpCount = 0
    disAppearIpCount = 0
    ipChangeCount = 0
    validIpCount = 0
    for domain, ips in deq[0].items():
        if len(ips) == 0:
            if len(deq[1][domain]) > 0 and len(deq[2][domain]) > 0 and len(deq[3][domain]) > 0:
                newIpCount += 1
                domainChangeCount[domain][0] += 1
                domainChangeCount[domain][1] += 1
        elif len(deq[1][domain]) == 0 and len(deq[2][domain]) == 0 and len(deq[3][domain]) == 0:
            disAppearIpCount += 1
            domainChangeCount[domain][0] += 1
            domainChangeCount[domain][2] += 1
        else:
            firstIp = ips["0"]
            if firstIp not in deq[1][domain].keys() and firstIp not in deq[2][domain].keys() and firstIp not in deq[3][domain].keys():
                ipChangeCount += 1
                domainChangeCount[domain][0] += 1
                domainChangeCount[domain][3] += 1
        if len(deq[1][domain]) > 0 or len(deq[2][domain]) > 0 or len(deq[3][domain]) > 0:
            validIpCount += 1
    deq.popleft()

    message = str(i-2)+","+str((i-2)/3.0)+","
    message += str(validIpCount*100.0/totalIpCount)+","
    message += str(newIpCount*100.0/totalIpCount)+","
    message += str(disAppearIpCount*100.0/totalIpCount)+","
    message += str(ipChangeCount*100.0/totalIpCount)+","
    print (message)

sorted_list = sorted(domainChangeCount.items(), key=lambda x: x[1][0], reverse=True)
with open('changeDomainsSlidingWindow.txt', 'w') as fp:
    fp.write('\n'.join('%s %s' % x for x in sorted_list))
