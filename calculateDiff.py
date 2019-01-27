import json

domainIpDict = {}
with open('RR0.json') as f:
    rr = f.readlines()
repeatedDomains = {}
for line in rr:
    data = json.loads(line)
    domain = data["name"]
    if domain in domainIpDict.keys():
        repeatedDomains[domain] = 1
        continue
    domainIpDict[domain] = {}
    if data["status"] != "NOERROR":
        continue
    for ip in data["data"]["ipv4_addresses"]:
        domainIpDict[domain][ip] = 1

print ("Unique Domain Count: " + str(len(domainIpDict)))
differences = []
for i in range(1, 16):
    differenceCount = 0
    for domain in repeatedDomains.keys():
        repeatedDomains[domain] = 1
    with open('RR'+str(i)+'.json') as f:
        rr = f.readlines()
    for line in rr:
        data = json.loads(line)
        domain = data["name"]
        if domain in repeatedDomains.keys():
            if repeatedDomains[domain] == 1:
                repeatedDomains[domain] = 0
            else:
                continue
        if data["status"] != "NOERROR":
            if len(domainIpDict[domain]) > 0:
                differenceCount += 1
            continue
        if data["data"]["ipv4_addresses"][0] not in domainIpDict[domain].keys():
            differenceCount += 1
    print(i)
    print(differenceCount)
    differences.append(differenceCount)

print (differences)
