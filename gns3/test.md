###  
```bash

# ip link add name br0 type bridge
# ip link set eth0  master br0
# ip link set eth1  master br0
# ip link set eth2  master br0
# ip addr add 10.0.1.1/24 dev br0
# ip link set dev br0 up
# ip link del 10.0.1.1/24 br0

# ip addr del 192.168.1.92/24 dev eth0









#switch 1

# #eth0,1,2
# ip link add name br0 type bridge
# ip link add link br0 name br0.10 type vlan id 10
# ip link set eth0  master br0
# ip link set eth1 master br0
# ip link set eth2  master br0
# ip link set dev br0 up
# ip addr add 10.0.1.252/24 dev br0.10
# ip link set dev br0.10 up

# #eth23
# ip link add name br99 type bridge
# ip link add link br99 name br99.10 type vlan id 10
# ip link add link br99 name br99.20 type vlan id 20
# ip link add link br99 name br99.30 type vlan id 30
# ip link set eth23  master br99
# ip link set dev br99 up

# ip addr add 10.0.1.254/24 dev br99.10
# ip addr add 10.0.2.254/24 dev br99.20
# ip addr add 10.0.3.254/24 dev br99.30

# ip link set dev br99.10 up
# ip link set dev br99.20 up
# ip link set dev br99.30 up

```
#### PC
```bash
#pc1
ip link add name br0 type bridge
ip link set eth0 master br0
ip addr add 10.0.1.3/24 dev br0
ip link set dev br0 up
```


#### Trunk 
```bash
#switch 1
ovs-vsctl add-br  br0
ovs-vsctl add-port br0 eth0 tag=10 
ovs-vsctl add-port br0 eth1 tag=10 
ovs-vsctl add-port br0 eth2 tag=20 
ovs-vsctl add-port br0 eth3 tag=20 
ovs-vsctl add-port br0 eth24 trunk=10,20
```

```bash
#switch 2
ovs-vsctl add-br  br0
ovs-vsctl add-port br0 eth0 tag=10 
ovs-vsctl add-port br0 eth1 tag=20
ovs-vsctl add-port br0 eth3 trunk=10,20
```

```bash  
#
# iptables -t mangle -A PREROUTING -s 10.0.1.2 -d 10.0.1.200 -o eth0 -j MARK --set-mark 1
# ip rule add fwmark 1 table 100
# echo "100 wan1" >> /etc/iproute2/rt_tables
# ip route add default via 192.168.1.2 dev eth0 table wan1

# iptables -t mangle -A PREROUTING -s 10.0.1.201 -d 10.0.1.254 -o eth1 -j MARK --set-mark 2
# ip rule add fwmark 2 table 200
# echo "200 wan2" >> /etc/iproute2/rt_tables
# ip route add default via 192.168.1.3 dev eth1 table wan2

```

```bash

ovs-vsctl add-br br1
ovs-vsctl add-port br0 eth0
ovs-ofctl add-flow br0 priority=100,ip,nw_src=10.0.1.2/32,nw_dst=192.168.1.2/32,actions=output:1
ovs-ofctl add-flow br0 priority=100,ip,nw_src=10.0.1.3/32,nw_dst=192.168.1.3/32,actions=output:2



```


### ofctl
```bash
# actions output number is list index
ovs-vsctl list-ports br0

#must delete the ports associated with the bridge first.
ovs-vsctl del-port br0 eth0


ovs-vsctl add-port br1 p1 -- set Interface p1 type=internal
#show 
ovs-ofctl dump-flows br1

# do not repeat Interface name,ofport=1 defind the  port number become to  1
ovs-vsctl add-port br0 eth3 -- set Interface eth3 ofport=1

ovs-ofctl del-flows br0 "in_port=1"


ovs-ofctl add-flow br0 "priority=100, in_port=1, actions=output:2"
```

### example

```bash

#查看br-tun中OpenFlow flows
ovs-ofctl dump-flows br-tun
#查看br-tun端口信息   
ovs-ofctl show br-tun
#添加新的flow：对于从端口p0进入交换机的数据包，如果它不包含任何VLAN tag，则自动为它添加VLAN tag 101

# idle_timeout=1000 life time
ovs-ofctl add-flow br0 "priority=3,in_port=100,dl_vlan=0xffff,actions=mod_vlan_vid:101,normal"
#对于从端口3进入的数据包，若其vlan tag为100，去掉其vlan tag，并从端口1发出 
ovs-ofctl add-flow br0 in_port=3,dl_vlan=101,actions=strip_vlan,output:1
#添加新的flow: 修改从端口p1收到的数据包的源地址为9.181.137.1,show 查看p1端口ID为100   
ovs-ofctl add-flow br0 "priority=1 idle_timeout=0,in_port=100,actions=mod_nw_src:9.181.137.1,normal"
#添加新的flow: 重定向所有的ICMP数据包到端口 p2
ovs-ofctl add-flow br0 idle_timeout=0,dl_type=0x0800,nw_proto=1,actions=output:102
#删除编号为 100 的端口上的所有流表项   
ovs-ofctl del-flows br0 "in_port=100"   
```


```bash
# principle of vlan
# 客户端访问服务端
ovs-ofctl add-flow ovsBusiness "cookie=0,priority=40001,ip,in_port=1,dl_vlan=10,nw_src=1.1.1.12,nw_dst=1.1.1.13 actions=strip_vlan,output:3"
ovs-ofctl add-flow ovsBusiness "cookie=0,priority=40001,ip,in_port=4,nw_src=1.1.1.12,nw_dst=1.1.1.13 actions=mod_vlan_vid:10,output:2"
# 服务端相应客户端请求
ovs-ofctl add-flow ovsBusiness "cookie=0,priority=40001,ip,in_port=2,dl_vlan=10,nw_src=1.1.1.13,nw_dst=1.1.1.12 actions=strip_vlan,output:4"
ovs-ofctl add-flow ovsBusiness "cookie=0,priority=40001,ip,in_port=3,nw_src=1.1.1.13,nw_dst=1.1.1.12 actions=mod_vlan_vid:10,output:1"
# 放通arp数据包
ovs-ofctl add-flow ovsBusiness "cookie=0,priority=40001,arp,in_port=1 actions=output:3"
ovs-ofctl add-flow ovsBusiness "cookie=0,priority=40001,arp,in_port=4 actions=output:2"
ovs-ofctl add-flow ovsBusiness "cookie=0,priority=40001,arp,in_port=2 actions=output:4"
ovs-ofctl add-flow ovsBusiness "cookie=0,priority=40001,arp,in_port=3 actions=output:1"
```


```bash
# table
# https://zhuanlan.zhihu.com/p/37408341
# from table0 to table1
ovs-ofctl add-flow vswitch0 "table=0,actions=goto_table=1"
#set table1 to group1
ovs-ofctl -O OpenFlow13 add-group vswitch0 "group_id=1,type=select,bucket=resubmit(,1)"
# flow from table0 to group1 
ovs-ofctl -O OpenFlow13 add-flow vswitch0 "table=0,in_port=1,actions=group:1"
ovs-ofctl -O OpenFlow13 add-flow vswitch0 "table=0,in_port=4,actions=group:1"
# 匹配进端口为1的流量，经过meter表限速，然后转发到2端口
ovs-ofctl add-flow s1 priority=200,in_port=1,action=meter:1,output:2 -O OpenFlow13
# 匹配源mac地址：78:45:c4:1c:ba:b9，目的mac地址：00:50:56:c0:00:08，动作是丢弃
ovs-ofctl add-flow br0 dl_src=78:45:c4:1c:ba:b9,dl_dst=00:50:56:c0:00:08,aciton=drop
```

#### test 
```bash
#test 
ovs-vsctl add-br br0
# ovs-vsctl del-br br0

# ip addr add 10.0.1.2/24 dev eth0
# ip addr del 10.0.1.2/24 dev eth0
ovs-vsctl add-port br0 eth0
# ovs-vsctl del-port br0 eth0

# ip addr add 10.0.1.3/24 dev eth1
# ip addr del 10.0.1.3/24 dev eth1
ovs-vsctl add-port br0 eth1
# ovs-vsctl del-port br0 eth1

# ip addr add 10.0.2.2/24 dev eth2
# ip addr del 10.0.2.2/24 dev eth2
ovs-vsctl add-port br0 eth2
# ovs-vsctl del-port br0 eth3

ovs-vsctl show
ovs-ofctl dump-flows br0
ovs-ofctl del-flows br0 "table=0"

# ovs-ofctl add-flow table=0 nw_src=10.0.1.2 actions=mod_nw_src:10.0.1.2
```

```bash
#pc1
ip link add name br0 type bridge
ip link set eth0 master br0
ip addr add 10.0.2.2/24 dev br0
ip link set dev br0 up
# ip link del br0

#pc2
ip link add name br0 type bridge
ip link set eth0 master br0
ip addr add 10.0.2.3/24 dev br0
ip link set dev br0 up
# ip link del br0

#pc3
ip link add name br0 type bridge
ip link set eth0 master br0
ip addr add 10.0.1.2/24 dev br0
ip link set dev br0 up
# ip link del br0


#pc4
ip link add name br0 type bridge
ip link set eth0 master br0
ip addr add 10.0.1.3/24 dev br0
ip link set dev br0 up
# ip link del br0



#pc100
ip link add name br0 type bridge
ip link set eth0 master br0
ip addr add 10.0.2.4/24 dev br0
ip link set dev br0 up
# ip link del br0

ip link add name br1 type bridge
ip link set eth1 master br1
ip addr add 10.0.2.5/24 dev br1
ip link set dev br1 up
# ip link del br1








#test  cross subnet
# ovs-ofctl dump-flows br0
# ovs-ofctl del-flows br0 "table=0"

#设置ovs模式为secure.  因为standalone 在三次探测控制器连接不成功ovs后,-vswitchd会会接管转发逻辑自动配置新的转发流表
#switch 1 
ip addr add 10.0.2.1/24 dev br0
ip link set dev br0 up
ovs-ofctl del-flows br0 "table=0"

#switch 2

ip addr add 10.0.1.1/24 dev br0
ip link set dev br0 up
ovs-ofctl del-flows br0 "table=0"


##pc自己的mac地址,pc 10.0.2.2从port1出,ovs-ofctl show br0看port对应网口连接哪个pc
#switch 1  
ovs-ofctl add-flow br0 "ip,nw_dst=10.0.2.2,actions=mod_dl_dst:f2:52:fb:97:0b:28,output:1"
ovs-ofctl add-flow br0 "ip,nw_dst=10.0.2.3,actions=mod_dl_dst=ee:82:9e:16:9d:09,output:2"

#switch 2
ovs-ofctl add-flow br0 "ip,nw_dst=10.0.1.2,actions=mod_dl_dst:62:23:92:e6:24:fc,output:1"
ovs-ofctl add-flow br0 "ip,nw_dst=10.0.1.3,actions=mod_dl_dst=12:03:cb:a6:3d:ba,output:2"


#把目标地址为 10.0.2.2的arp包从port1发出,把目标地址为 10.0.2.3的arp包从port2发出  switch1
ovs-ofctl add-flow br0 "priority=100,arp,arp_tpa=10.0.2.2,actions=output:1"
ovs-ofctl add-flow br0 "priority=100,arp,arp_tpa=10.0.2.3,actions=output:2"
#switch2
ovs-ofctl add-flow br0 "priority=100,arp,arp_tpa=10.0.1.2,actions=output:1"
ovs-ofctl add-flow br0 "priority=100,arp,arp_tpa=10.0.1.3,actions=output:2"


#arp switch1 
ovs-ofctl add-flow br0 "priority=65535,arp,arp_tpa=10.0.2.1,actions=NORMAL"
ovs-ofctl add-flow br0 "priority=200,ip,nw_dst=10.0.2.1,actions=NORMAL"
#switch2 
ovs-ofctl add-flow br0 "priority=65535,arp,arp_tpa=10.0.1.1,actions=NORMAL"
ovs-ofctl add-flow br0 "priority=200,ip,nw_dst=10.0.1.1,actions=NORMAL"

#牛头不对马嘴
# #arp switch 1
#把arp包目标地址为10.0.1.2的mac地址修改为网关10.0.1.1 mac地址, 从port3发出
ovs-ofctl add-flow br0 "arp,arp_tpa=10.0.1.2  actions=mod_dl_src:fe:be:98:55:24:4e,output:3"
#把目标地址为10.0.1.0的源mac地址修改为网关10.0.1.1 mac地址, 从port3发出
#把目标地址为10.0.1.0的目标mac地址修改为网关10.0.2.1 mac地址, 从port3发出
ovs-ofctl add-flow br0 "ip,nw_dst=10.0.1.0/24 actions=mod_dl_src:fe:be:98:55:24:4e,mod_dl_dst:fa:fe:5a:bc:18:4f,dec_ttl,output:3"



# #arp switch 2
ovs-ofctl add-flow br0 "priority=1,arp,arp_tpa=10.0.2.2 actions=mod_dl_src:fa:fe:5a:bc:18:4f,output:3"
ovs-ofctl add-flow br0 "ip,nw_dst=10.0.2.2  actions=mod_dl_src:fa:fe:5a:bc:18:4f,output:3"

```