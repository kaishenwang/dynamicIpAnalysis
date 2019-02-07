import json
from os import listdir
from os.path import isfile, join
from collections import deque

folderPath = "/home/kwang40/alookupResult/"
deq = deque(maxlen=3)

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
totalIpCount = 0
with open(join(folderPath, files[0])) as f:
    rr = f.readlines()
for line in rr:
    totalIpCount += 1
    data = json.loads(line)
    if data["status"] == "NOERROR":
        domainIpDict[data["name"]] = data["data"]["ipv4_addresses"][0]
    else:
        domainIpDict[data["name"]] = ""


updateDeq(join(folderPath, files[1]))
updateDeq(join(folderPath, files[2]))

for i in range(3, min(len(files),24*5*3)):
    updateDeq(join(folderPath, files[i]))
    newIpCount = 0
    disAppearIpCount = 0
    ipChangeCount = 0
    validIpCount = 0
    for domain,ip in domainIpDict.items():
        if len(ip) == 0:
            if len(deq[0][domain]) > 0 and len(deq[1][domain]) > 0 and len(deq[2][domain]) > 0:
                newIpCount += 1
        elif len(deq[0][domain]) == 0 and len(deq[1][domain]) == 0 and len(deq[2][domain]) == 0:
            disAppearIpCount += 1
        else:
            firstIp = domainIpDict[domain]
            changeIp = True
            for d in deq:
                if firstIp in d[domain].keys():
                    changeIp = False
                    break
            if changeIp:
                ipChangeCount += 1
        if len(deq[0][domain]) > 0 or len(deq[1][domain]) > 0 or len(deq[2][domain]) > 0:
            validIpCount += 1
    message = str(i)+","+str(i/3.0)+","
    message += str(validIpCount*100.0/len(domainIpDict))+","
    message += str(newIpCount*100.0/len(domainIpDict))+","
    message += str(disAppearIpCount*100.0/len(domainIpDict))+","
    message += str(ipChangeCount*100.0/len(domainIpDict))+","
    print (message)
