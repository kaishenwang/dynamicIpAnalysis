import sys
import json
#python buildZmapOut.py RR.json banner.json  zmap.txt
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
        if line[:4] != 'null':
            data = json.loads(line)
            IPs[data['ip']] = True

with open(sys.argv[3],'w') as wf:
    for k,v in IPs.items():
        if v:
            wf.write(k + ',80,' + 'true\n')
        else:
            wf.write(k + ',80,' + 'false\n')
