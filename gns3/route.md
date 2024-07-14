```bash
等于更改本机ip 同个网桥直接ping 
sudo ip addr add 192.168.0.2/24 dev eth0
sudo ip link set eth0 up
sudo ip route add default via 192.168.0.1
```

```bash
路由
ip addr add 192.168.0.1/24 dev eth0
ip link set eth0 up

路由
ip addr add 192.168.2.1/24 dev eth1
ip link set eth1 up

```
```bash
bash -c 'echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf'
```


