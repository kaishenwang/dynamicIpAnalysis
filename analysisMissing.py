import json

openIP = {}
with open('IPOpen.txt') as f:
    for line in f:
        openIP[line.rstrip()] = True

with open('RR.json') as f, open('noOpenPortDomains.txt', 'w') as wf:
    for line in f:
        try:
            data = json.loads(line.rstrip())
            if data['status'] == 'NOERROR':
                ip = data['data']['ipv4_addresses'][0]
                if ip not in openIP:
                    wf.write(ip + '\n')
        except:
            continue

httpCode = {}
with open('banners.json') as f, open('noHttpDomains.txt', 'w') as wf:
    for line in f:
        if line[:4] == 'null':
            continue
        data = json.loads(line.rstrip())
        code = -1
        if 'response' in data['data']['http']:
            code = data['data']['http']['response']['status_code']
        elif 'redirect_response_chain' in  data['data']['http']:
            code = data['data']['http']['redirect_response_chain'][0]['status_code']
        else:
            wf.write(data['domain'] + ',' + data['error'].encode('ascii', 'ignore').decode('ascii') + '\n')
        if code > 0:
            if code not in httpCode:
                httpCode[code] = 0
            httpCode[code] += 1

sorted_code = sorted(httpCode.items(), key=lambda x: x[1], reverse=True)
with open('httpCode.txt', 'w') as wf:
    for k,v in sorted_code:
        wf.write(str(k) + ',' + str(v) + '\n')
