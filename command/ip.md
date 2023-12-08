#
##
### bridge
```bash
# delete bridge[label](admin:/root/GNS3/projects/vlan_test/readme.md)
ip link delete br0
#show 

ip link show 
#add [label](admin:/root/GNS3/projects/vlan_test/readme.md)
ip link add name br0 type bridge
#set eth to bridge
ip link set eth2  master br0

#set eth2 without master
ip link set eth2 nomaster
```

#### bridge example
```bash
# ovs-route-3:10.0.1.0/16
ip link add name br0 type bridge
ip link set eth2  master br0
ip link set eth3  master br0
ip link set eth4  master br0
ip link set eth5  master br0
ip link set eth6  master br0
ip addr add 10.0.1.1/16 dev br0
sysctl net.ipv4.ip_forward=1
sysctl net.ipv4.conf.default.rp_filter=0
sysctl net.ipv4.conf.all.rp_filter=0
iptables -I FORWARD -m physdev --physdev-is-bridged -j ACCEPT
ip link set dev br0 up

#wan0
iptables -t nat -A POSTROUTING -s 10.0.1.0/16 -o eth0 -j MASQUERADE
ifconfig eth0 192.168.1.92 netmask 255.255.255.0
route add default gw 192.168.1.1
ifconfig eth0 up


```

```bash
# ovs-route-2:10.0.2.0/16
ip link add name br0 type bridge
ip link set eth2  master br0
ip link set eth3  master br0
ip link set eth4  master br0
ip link set eth5  master br0
ip link set eth6  master br0
ip addr add 10.0.2.1/16 dev br0
sysctl net.ipv4.ip_forward=1
sysctl net.ipv4.conf.default.rp_filter=0
sysctl net.ipv4.conf.all.rp_filter=0
iptables -I FORWARD -m physdev --physdev-is-bridged -j ACCEPT
ip link set dev br0 up

#wan0
iptables -t nat -A POSTROUTING -s 10.0.2.0/16 -o eth0 -j MASQUERADE
ifconfig eth0 192.168.1.92 netmask 255.255.255.0
route add default gw 192.168.1.1
ifconfig eth0 up
```

```bash



```

<!-- 
ip route add 10.0.2.0/16 via 10.0.2.1
ip route add 192.168.1.0/24 via 192.168.1.1 -->



```bash  
#ovs-route-1:192.168.1.0/24
ip link add name br0 type bridge
ip link set eth2  master br0
ip link set eth3  master br0
ip link set eth4  master br0
ip link set eth5  master br0
ip link set eth6  master br0
ip addr add 192.168.1.1/24 dev br0
sysctl net.ipv4.ip_forward=1
sysctl net.ipv4.conf.default.rp_filter=0
sysctl net.ipv4.conf.all.rp_filter=0
iptables -I FORWARD -m physdev --physdev-is-bridged -j ACCEPT
ip link set dev br0 up
```


```bash  
#ovs-route-1:10.0.3.0/16
ip link add name br0 type bridge
ip link set eth2  master br0
ip link set eth3  master br0
ip link set eth4  master br0
ip link set eth5  master br0
ip link set eth6  master br0
ip addr add 10.0.3.1/16 dev br0
sysctl net.ipv4.ip_forward=1
sysctl net.ipv4.conf.default.rp_filter=0
sysctl net.ipv4.conf.all.rp_filter=0
iptables -I FORWARD -m physdev --physdev-is-bridged -j ACCEPT
ip link set dev br0 up

#wan0
iptables -t nat -A POSTROUTING -s 10.0.3.0/16 -o eth0 -j MASQUERADE
ifconfig eth0 192.168.0.92 netmask 255.255.255.0
route add default gw 192.168.0.1
ifconfig eth0 up
```

```bash  
#ovs-route-1:192.168.0.0/24
ip link add name br0 type bridge
ip link set eth2  master br0
ip link set eth3  master br0
ip link set eth4  master br0
ip link set eth5  master br0
ip link set eth6  master br0
ip addr add 192.168.0.1/24 dev br0
sysctl net.ipv4.ip_forward=1
sysctl net.ipv4.conf.default.rp_filter=0
sysctl net.ipv4.conf.all.rp_filter=0
iptables -I FORWARD -m physdev --physdev-is-bridged -j ACCEPT
ip link set dev br0 up
```