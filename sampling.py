import sys
import random

targetSampling = 50000
inputFile = '/data1/nsrg/kwang40/2019-01-17-urls.txt'
outputFile = sys.argv[1]

with open(inputFile) as f:
    domainSet = f.readlines()

ratio = len(domainSet) / targetSampling

outputSize = 0
with open (outputFile, 'w') as f:
    for i in range(domainSet):
        if random.randint(1,ratio) == 1:
            f.write(domainSet[i] + "\n")
            outputSize += 1
            if outputSize == targetSampling:
                break
