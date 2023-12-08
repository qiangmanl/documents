#  
##
### download from https://github.com/seaweedfs/seaweedfs/releases  https://ghproxy.com/ by input resource url.
### copy type
```
000 no replication, just one copy
001 replicate once on the same rack
010 replicate once on a different rack in the same data center
100 replicate once on a different data center
200 replicate twice on two other different data center
110 replicate once on a different rack, and once on a different data center

```
./weed -v=3 master -port=8100 -mdir=./master8100 -peers=qiangmanl.com:8100,qiangmanl.com:8101,qiangmanl.com:8102 -defaultReplication=100 >> ./master8100/master8100.log &
./weed -v=3 master -port=8101 -mdir=./master8101 -peers=qiangmanl.com:8100,qiangmanl.com:8101,qiangmanl.com:8102 -defaultReplication=100 >> ./master8100/master8100.log &
./weed -v=3 master -port=8102 -mdir=./master8102 -peers=qiangmanl.com:8100,qiangmanl.com:8101,qiangmanl.com:8102 -defaultReplication=100 >> ./master8100/master8100.log &

./weed -v=3 volume -port=8200 -dir=./v1 -mserver=localhost:8100 -dataCenter=dc1 >>./master8100/master8100.log &
./weed -v=3 volume -port=8201 -dir=./v2 -mserver=localhost:8101 -dataCenter=dc2 >>./master8100/master8100.log &
./weed -v=3 volume -port=8202 -dir=./v3 -mserver=localhost:8102 -dataCenter=dc3 >>./master8100/master8100.log &