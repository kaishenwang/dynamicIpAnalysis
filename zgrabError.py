import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
#lines = [x.rstrip() for x in lines]

connectionError = {}
commonErrors = ['certificate is valid', 'oversized record received', 'malformed HTTP response', 'malformed HTTP status code']
for line in lines:
    errorStart = line.find('[ERROR]')
    if errorStart == -1:
        continue
    infoStart = errorStart + len('[ERROR] banner-grab:')
    httpStart = max(infoStart, line.find('http'))
    detailMessage = line.rfind(':') + 2
    key = line[infoStart:httpStart] + "/"
    notSet = True
    for commonError in commonErrors:
        if line[detailMessage:detailMessage+len(commonError)] == commonError:
            key += commonError
            notSet = False
            break
    if notSet:
        key += line[detailMessage : -1]
    #key = line[infoStart:httpStart] + "/" + line[detailMessage+2:-1]
    connectionError[key] = connectionError.get(key, 0) + 1

sorted_list = sorted(connectionError.items(), key=lambda x: x[1], reverse=True)
for v in sorted_list:
    print (v)
