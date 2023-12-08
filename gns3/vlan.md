```bash
#不可以在ip link 里设置br，已经有的要删除再通过 ovs-vsctl 添加
ovs-vsctl del-br br01
ovs-vsctl add-br br01
ovs-vsctl show
#已经加入其他bridge不可以再加入，就是等于dev被master到bridge
ovs-vsctl add-port br01 eth3 tag=1
ovs-vsctl add-port br01 eth2 tag=1

#已经master到br0的dev eth0可以在ip link里看到，但是ovs认不到需要从br0删除
ip link set dev eth0 nomaster

#再把dev eth0添加到vlan tag 
ovs-vsctl add-port br01 eth0 tag=2
ip link set dev eth1 nomaster

ovs-vsctl add-br br02
ovs-vsctl add-port br02 eth0 tag=2

#此时的eth0和eth1虽然tag都为2，但是不在同一个bridge，所以ping不通
#只有当连接设备都连接在同一个br下设置不同的tag才有意义，不然不同的br本身是无法通信的

```
