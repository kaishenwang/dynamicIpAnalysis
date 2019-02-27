#cd /home/kwang40/go/src/github.com/kwang40/pipelineWrapper
cd /home/kwang40/zmap
make
mkdir /data1/nsrg/kwang40/fullData/$(date -u +\%Y-\%m-\%d)
cd /data1/nsrg/kwang40/fullData/$(date -u +\%Y-\%m-\%d)
ulimit -n 65536
/home/kwang40/go/src/github.com/kwang40/pipelineWrapper/pipelineWrapper --url-file=/data1/nsrg/kwang40/2019-01-17-urls.txt --zdns-excutable=/home/kwang40/go/src/github.com/kwang40/zdns/zdns/./zdns --zmap-excutable=/home/kwang40/zmap/src/./zmap | /home/kwang40/go/src/github.com/kwang40/zgrab/./zgrab --port 80 --http=/ --fullURL=true --output-file=banners.json --http-max-redirects=10 2>zgrabError.txt 1>result.txt
