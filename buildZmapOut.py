import sys
import json
#python buildZmapOut.py RR.json IPOpen.txt  zmap.txt
IPs = {}
with open (sys.argv[1]) as f:
    for line in f:
        try:
            data = json.loads(line)
            if data['status'] == 'NOERROR':
                IPs[data['data']['ipv4_addresses'][0]] = False
        except:
            continue

with open(sys.argv[2]) as f:
    for line in f:
        IPs[line.rstrip()] = True

with open(sys.argv[3],'w') as wf:
    for k,v in IPs.items():
        if v:
            wf.write(k + ',80,' + 'true\n')
        else:
            wf.write(k + ',80,' + 'false\n')
