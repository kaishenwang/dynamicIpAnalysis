import json
import sys

domainIpDict = {}
with open(sys.argv[1]) as f:
    rr = f.readlines()

noErrorCount = 0
noAnswerCount = 0
for line in rr:
    data = json.loads(line)
    if data["status"] == "NOERROR":
        noErrorCount += 1
    elif data["status"] == "NO_ANSWER":
        noAnswerCount += 1
print ("No Error:"  + str(noErrorCount))
print ("No Answer:" + str(noAnswerCount))
