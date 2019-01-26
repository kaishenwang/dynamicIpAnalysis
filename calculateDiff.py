import json

domainIpDict = {}
with open('RR0.json') as f:
    rr = f.readlines()

for line in rr:
    data = json.loads(line)
    domain = data["name"]
    domainIpDict[domain] = {}
    if data["status"] != "NOERROR":
        continue
    for ip in data["data"]["ipv4_addresses"]:
        domainIpDict[domain][ip] = 1

differences = []
for i in range(1, 16):
    differenceCount = 0
    with open('RR'+str(i)+'.json') as f:
        rr = f.readlines()
    for line in rr:
        data = json.loads(line)
        domain = data["name"]
        if data["status"] != "NOERROR":
            if len(domainIpDict[domain] > 0):
                differenceCount += 1
            continue
            if data["data"]["ipv4_addresses"][0] not in domainIpDict[domain].keys():
                differenceCount += 1
    differences.append(differenceCount)

    print (differences)
