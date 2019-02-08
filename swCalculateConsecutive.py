import json
from os import listdir
from os.path import isfile, join
import copy
from operator import itemgetter
from collections import deque

folderPath = "/home/kwang40/alookupResult/"
deq = deque(maxlen=6)

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


for i in range(6):
    updateDeq(join(folderPath, files[i]))

# new ip: previous three has no valid ip (i compare to i-1, i-2, i-3)
#         compare 3 to 0,1,2
# disappear ip: previous one has valid ip, next three (including this one)
#              has no valid ip (i-1 compare to i, i+1, i+2)
#              compare 2 to 3,4,5
# change ip: previous ip[0] not in next three ips (i-1 compare to i, i+1, i+2)
#            compare 2 to 3,4,5
# vaid ip: have valid ip in i, i+1, i+2
#          check 3,4,5
# keep a deque of length 6, after analyze, update data in i+3
for i in range(3, min(5*24*3,len(files))-3):
    newIpCount = 0
    for domain, ips in deq[3].items():
        if len(ips) > 0 and len(deq[0][domain]) == 0 and len(deq[1][domain]) == 0 and len(deq[2][domain]) == 0:
            newIpCount += 1
            domainChangeCount[domain][0] += 1
            domainChangeCount[domain][1] += 1
    disAppearIpCount = 0
    ipChangeCount = 0
    validIpCount = 0
    for domain, ips in deq[2].items():
        validIp = (len(deq[3][domain]) > 0 or len(deq[4][domain]) > 0 or len(deq[5][domain]) > 0)
        if validIp:
            validIpCount += 1
        if len(ips) > 0:
            if not validIp:
                disAppearIpCount += 1
                domainChangeCount[domain][0] += 1
                domainChangeCount[domain][2] += 1
                firstIp = ips['0']
            else:
                if firstIp not in deq[3][domain].keys() and firstIp not in deq[4][domain].keys() and firstIp not in deq[5][domain].keys():
                    ipChangeCount += 1
                    domainChangeCount[domain][0] += 1
                    domainChangeCount[domain][3] += 1

    message = str(i)+","+str((i)/3.0)+","
    message += str(validIpCount*100.0/totalIpCount)+","
    message += str(newIpCount*100.0/totalIpCount)+","
    message += str(disAppearIpCount*100.0/totalIpCount)+","
    message += str(ipChangeCount*100.0/totalIpCount)+","
    print (message)
    updateDeq(join(folderPath, files[i+3]))

sorted_list = sorted(domainChangeCount.items(), key=lambda x: x[1][0], reverse=True)
with open('changeDomainsSlidingWindow.txt', 'w') as fp:
    fp.write('\n'.join('%s %s' % x for x in sorted_list))
