```bash
#stop  7890 port from clash proxy
sudo su
nerdctl pull docker.io/coredns/coredns:latest

# <!-- nerdctl run -d --name coredns -p 5353:53/udp -p 5353:53/tcp -v /path/to/Corefile:/etc/coredns/Corefile coredns/coredns -->

# <!-- nerdctl create --name ihotel-dns \
#     --net bridge \
#     -p 58:53/udp -p 58:53/tcp\
#     docker.io/coredns/coredns:latest -->



# <!-- . {
#     forward . 8.8.8.8
#     zone "qiangmanl.com" {
#         type master
#         file /etc/coredns/qiangmanl.com.db
#     }
# } -->

sudo lsof -i :53
sudo systemctl stop systemd-resolved.service 



#if coredns donot work, keep systemd-resolved.service  up 
sudo systemctl start systemd-resolved.service 
docker pull coredns/coredns
docker run -d --name ihotel-dns    -p 53:53/udp -p 53:53/tcp  --restart always    -v /home/yang/coredns:/etc/coredns   coredns/coredns  -conf /etc/coredns/Corefile

#DNS server


/etc/services change udp,tcp port 
#
dig @127.0.0.1 -p 53 ihotel.lo


```
###  resolve
> https://juejin.cn/post/7099327481626230792