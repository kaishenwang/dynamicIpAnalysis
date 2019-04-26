cd /home/kwang40/zmap
make
mkdir /data1/nsrg/kwang40/completeData/$(date -u +\%Y-\%m-\%d)
cd /data1/nsrg/kwang40/completeData/$(date -u +\%Y-\%m-\%d)
ulimit -n 65536
python3 /home/kwang40/dynamicIpAnalysis/extractEffectiveURL.py  /data1/nsrg/domain_blacklists/parsed/$(date -u +\%Y-\%m-\%d-)blacklist-entries.csv
/home/kwang40/go/src/github.com/kwang40/pipelineWrapper/pipelineWrapper --url-file=effectiveURL.txt --zdns-excutable=/home/kwang40/go/src/github.com/kwang40/zdns/zdns/./zdns --zmap-excutable=/home/kwang40/zmap/src/./zmap | /home/kwang40/go/src/github.com/kwang40/zgrab/./zgrab --port 80 --http=/ --full-url=true --output-file=banners.json --http-max-redirects=10 2>zgrabError.txt 1>result.txt
#/home/kwang40/go/src/github.com/kwang40/zdns/zdns/./zdns ALOOKUP -iterative --cache-size=500000 --input-file=randSubURL.txt --output-file=randSubDomainRR.json
python /home/kwang40/dynamicIpAnalysis/buildZmapOut.py RR.json IPOpen.txt zmapOut.txt
cp RR.json /data1/nsrg/kwang40/parsedData/$(date -u +\%Y\%m\%d)-dns.json
cp zmapOut.txt /data1/nsrg/kwang40/parsedData/$(date -u +\%Y\%m\%d)-zmap.txt
cp banners.json /data1/nsrg/kwang40/parsedData/$(date -u +\%Y\%m\%d)-zgrab.json
