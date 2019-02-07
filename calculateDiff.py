import json
from os import listdir
from os.path import isfile, join

folderPath = "/home/kwang40/alookupResult/"
files = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]

files.sort()

domainIpDict = {}
totalIpCount = 0
with open(join(folderPath, files[0])) as f:
    rr = f.readlines()
for line in rr:
    totalIpCount += 1
    data = json.loads(line)
    domainIpDict[data["name"]] = ""
    if data["status"] == "NOERROR":
        domainIpDict[data["name"]] = data["data"]["ipv4_addresses"][0]


for i in range(1, min(len(files),24*5*3)):
    with open(join(folderPath, files[i])) as f:
        rr = f.readlines()
    newIpCount = 0
    disAppearIpCount = 0
    ipChangeCount = 0
    validIpCount = totalIpCount
    for line in rr:
        data = json.loads(line)
        domain = data["name"]
        if data["status"] != "NOERROR":
            validIpCount -= 1
            if len(domainIpDict[domain]) > 0:
                disAppearIpCount += 1
        elif len(domainIpDict[domain]) == 0:
            newIpCount += 1
        else:
            firstIp = domainIpDict[domain]
            changeIp = True
            for ip in data["data"]["ipv4_addresses"]:
                if firstIp == ip:
                    changeIp = False
                    break
            if changeIp:
                ipChangeCount += 1
    message = str(i)+","+str(i/3.0)+","
    message += str(validIpCount*100.0/totalIpCount)+","
    message += str(newIpCount*100.0/totalIpCount)+","
    message += str(disAppearIpCount*100.0/totalIpCount)+","
    message += str(ipChangeCount*100.0/totalIpCount)+","
    print (message)
