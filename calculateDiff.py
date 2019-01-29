import json
from os import listdir
from os.path import isfile, join

folderPath = "/home/kwang40/alookupResult/"
files = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]

files.sort()

domainIpDict = {}
validIpCount = 0
with open(join(folderPath, files[0])) as f:
    rr = f.readlines()
for line in rr:
    data = json.loads(line)
    domain = data["name"]
    domainIpDict[domain] = {}
    if data["status"] != "NOERROR":
        validIpCount += 1
        continue
    for ip in data["data"]["ipv4_addresses"]:
        domainIpDict[domain][ip] = 1
print(str(validIpCount*100.0/len(domainIpDict)) +  "% has valid ip")

for i in range(1, len(files)):
    with open(join(folderPath, files[i])) as f:
        rr = f.readlines()
    newIpCount = 0
    disAppearIpCount = 0
    ipChangeCount = 0
    for line in rr:
        data = json.loads(line)
        domain = data["name"]
        if data["status"] != "NOERROR":
            if len(domainIpDict[domain]) > 0:
                disAppearIpCount += 1
        elif len(domainIpDict[domain]) == 0:
            newIpCount += 1
        elif data["data"]["ipv4_addresses"][0] not in domainIpDict[domain].keys():
            ipChangeCount += 1
    message = str(i * 1.0 / 3) + "hours: "
    message += "new ip " + str(newIpCount*100.0/len(domainIpDict)) + ", "
    message += "disappear ip " + str(disAppearIpCount*100.0/len(domainIpDict)) + ", "
    message += "ip value change " + str(ipChangeCount*100.0/len(domainIpDict))
    print (message)
