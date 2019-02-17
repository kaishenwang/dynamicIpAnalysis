from os import listdir
from os.path import isfile, join
import json
import sys

onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]

success_count = {}
totalCount = 0
for fileName in onlyfiles:
  if len(fileName) > 10 and fileName[-4:] == 'json':
    totalCount += 1
    with open(fileName) as f:
      rr = f.readlines()
    for line in rr:
      data = json.loads(line)
      domain = data["name"]
      if domain not in success_count:
        success_count[domain] = 0
      if data["status"] == "NOERROR":
        success_count[domain] += 1

distribute_count = {}
for k,v in success_count.items():
  if v not in distribute_count:
    distribute_count[v] = 0
  distribute_count[v] += 1

#print (totalCount)
#print (distribute_count)
for k,v in distribute_count.items():
    for i in range(v):
        sys.stdout.write(str(k)+',')
