```bash

ip link add name br0 type bridge
#eth0的桥接的转发和过滤操作由br0决定
ip link set eth0  master br0
ip link add name br1 type bridge
ip link set eth1  master br1


#设置地址
ip addr add 192.168.0.101/24 dev br0
ip link set br0 up

#当两设备需要在交换设备上的eth0和eth1两口之间通信时，交换机的设置
ip link add name br0 type bridge
ip link set eth0  master br0
ip link set eth1  master br0


#当在自己的设备上需要两口都可以与br连接时，设备上的设置
ip link set eth0  master br0
ip link set eth1  master br0



```
