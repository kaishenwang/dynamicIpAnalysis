import json
from os import listdir
from os.path import isfile, join
import copy
import math
from operator import itemgetter

folderPath = "/home/kwang40/alookupResult/"
files = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]

files.sort()

domainIpDict = {}
domainChangeCount = {}
validIpCount = 0
with open(join(folderPath, files[0])) as f:
    rr = f.readlines()
for line in rr:
    data = json.loads(line)
    domain = data["name"]
    domainIpDict[domain] = {}
    domainChangeCount[domain] = [0]*4
    if data["status"] == "NOERROR":
        validIpCount += 1
        for ip in data["data"]["ipv4_addresses"]:
            domainIpDict[domain][ip] = 1
print(str(validIpCount*100.0/len(domainIpDict)) +  "% has valid ip")

for i in range(1, min(2,len(files))):
    with open(join(folderPath, files[i])) as f:
        rr = f.readlines()
    newIpCount = 0
    disAppearIpCount = 0
    ipChangeCount = 0
    validIpCount = 0
    tmpDict = {}
    for line in rr:
        data = json.loads(line)
        domain = data["name"]
        tmpDict[domain] = {}
        if data["status"] == "NOERROR":
            validIpCount += 1
            for ip in data["data"]["ipv4_addresses"]:
                tmpDict[domain][ip] = 1
        if data["status"] != "NOERROR":
            if len(domainIpDict[domain]) > 0:
                disAppearIpCount += 1
                domainChangeCount[domain][0] += 1
                domainChangeCount[domain][2] += 1
        elif len(domainIpDict[domain]) == 0:
            newIpCount += 1
            domainChangeCount[domain][0] += 1
            domainChangeCount[domain][1] += 1
        elif data["data"]["ipv4_addresses"][0] not in domainIpDict[domain].keys():
            ipChangeCount += 1
            domainChangeCount[domain][0] += 1
            domainChangeCount[domain][3] += 1
    domainIpDict=copy.copy(tmpDict)
    message = str(i)+","+str(i/3.0)+","
    message += str(validIpCount*100.0/len(domainIpDict))+","
    message += str(newIpCount*100.0/len(domainIpDict))+","
    message += str(disAppearIpCount*100.0/len(domainIpDict))+","
    message += str(ipChangeCount*100.0/len(domainIpDict))+","
    print (message)

sorted_list = sorted(domainChangeCount.items(), key=lambda x: x[1][0])
with open('changeDomains.txt', 'w') as fp:
    fp.write('\n'.join('%s %s' % x for x in sorted_list))
