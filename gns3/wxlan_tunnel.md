 #
##
### bridge
```bash
# delete bridge
ip link delete br0
#show 

ip link show 
#add 
ip link add name br0 type bridge
#set eth to bridge
ip link set eth2  master br0

#set eth2 without master
ip link set eth2 nomaster


# show  ports to tags
ovs-vsctl show

# can not del internal br0  
ovs-vsctl del-port br0 eth1

#ovs-ofctl dump-flows br0 table=0

```



```bash
# 在以下的实例中1,2,3,4节点由于隧道打通，所以隧道互相通信，由于5没打通隧道，虽然在物理ip层互相通信，但是隧道内互不通信


#switch 
ovs-vsctl add-br vswitch
ovs-vsctl add-port vswitch eth0
ovs-vsctl add-port vswitch eth1
ovs-vsctl add-port vswitch eth2
ovs-vsctl add-port vswitch eth3
ovs-vsctl add-port vswitch eth4
ovs-vsctl add-port vswitch eth5
# node1
ovs-vsctl add-br br0
ovs-vsctl add-port br0 eth0
ifconfig br0 up
ifconfig br0 10.0.0.2 netmask 255.255.255.0 up


ovs-vsctl add-br br1
ifconfig br1 up
ifconfig br1 192.168.1.2  netmask 255.255.255.0 up 

# ovs-vsctl set interface vxlan1 options:remote_ip=192.0.2.2
# ovs-vsctl add-port br1 vxlan1 -- set interface vxlan1 type=vxlan options:remote_ip=10.0.0.3,10.0.0.4
ovs-vsctl add-port br1 vxlan1 -- set interface vxlan1 type=vxlan options:remote_ip="10.0.0.3"
ovs-vsctl add-port br1 vxlan2 -- set interface vxlan2 type=vxlan options:remote_ip="10.0.0.4"
ovs-vsctl add-port br1 vxlan3 -- set interface vxlan3 type=vxlan options:remote_ip="10.0.0.5"

# node2
ovs-vsctl add-br br0
ovs-vsctl add-port br0 eth0
ifconfig br0 up
ifconfig br0 10.0.0.3 netmask 255.255.255.0 up


ovs-vsctl add-br br1
ifconfig br1 up
ifconfig br1 192.168.1.3  netmask 255.255.255.0 up 
ovs-vsctl add-port br1 vxlan1 -- set interface vxlan1 type=vxlan options:remote_ip="10.0.0.2"

# node3
ovs-vsctl add-br br0
ovs-vsctl add-port br0 eth0
ifconfig br0 up
ifconfig br0 10.0.0.4 netmask 255.255.255.0 up

ovs-vsctl add-br br1
ifconfig br1 up
ifconfig br1 192.168.1.4  netmask 255.255.255.0 up 

ovs-vsctl add-port br1 vxlan2 -- set interface vxlan2 type=vxlan options:remote_ip="10.0.0.2"

#node4

ovs-vsctl add-br br0
ovs-vsctl add-port br0 eth0
ifconfig br0 up
ifconfig br0 10.0.0.5 netmask 255.255.255.0 up
ovs-vsctl add-br br1
ifconfig br1 up
ifconfig br1 192.168.1.5  netmask 255.255.255.0 up 
ovs-vsctl add-port br1 vxlan4 -- set interface vxlan4 type=vxlan options:remote_ip="10.0.0.2"

#node5
ovs-vsctl add-br br0
ovs-vsctl add-port br0 eth0
ifconfig br0 up
ifconfig br0 10.0.0.6 netmask 255.255.255.0 up
ovs-vsctl add-br br1
ifconfig br1 up
ifconfig br1 192.168.1.6  netmask 255.255.255.0 up 

#pc config
# 无法与隧道通信
auto eth0
iface eth0 inet static
	address 192.168.1.254
	netmask 255.255.255.0
	gateway 192.168.1.1
	up echo nameserver 192.168.1.1 > /etc/resolv.conf

