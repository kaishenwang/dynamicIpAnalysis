#!/bin/sh
cat sampleDomains.txt | ~/go/src/github.com/kwang40/zdns/./extract-fqdn | ~/go/src/github.com/kwang40/zdns/zdns/./zdns ALOOKUP -iterative -cache-size 100000 --output-file=RR$1.json
