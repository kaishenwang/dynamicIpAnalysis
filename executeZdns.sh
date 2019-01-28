#!/bin/sh
cat /home/kwang40/dynamicIpAnalysis/uniqueSampleDomains.txt | /home/kwang40/go/src/github.com/kwang40/zdns/zdns/./zdns ALOOKUP -iterative -cache-size 100000 --output-file=/home/kwang40/alookupResult/$(date -u +\%Y-\%m-\%dT\%H:\%M:\%S).json > /dev/null  2>&1
