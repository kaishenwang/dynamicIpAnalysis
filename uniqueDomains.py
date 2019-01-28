import sys

with open(sys.argv[1]) as f:
    domainSet = set(f.readlines())

for domain in domainSet:
    print(domain.rstrip())


