import subprocess
import time
import os

FNULL = open(os.devnull, 'w')
beginTime = time.time()
timeInterval = 900 # seconds
for i in range(16):
    executionTime = beginTime + i * timeInterval
    time.sleep(max(0, executionTime-time.time()))
    print ("Execute " + str(i) + " " + time.ctime())
    args = ["./executeZdns.sh"]
    args.append(str(i))
    subprocess.Popen(args, stdout=FNULL)
