## plugin

15306053857
### calico

#### install
```bash
cd /opt/cni/bin
curl -o calico -O -L "https://ghproxy.com/https://github.com/projectcalico/calicoctl/releases/download/v3.20.6/calicoctl-linux-amd64"
curl -o calico-ipam -O -L "https://ghproxy.com/https://github.com/projectcalico/cni-plugin/releases/download/v3.20.6/calico-ipam-amd64"
chmod +x calico 
chmod +x calico-ipam

```
#### /etc/cni/net.d conflist daemon
```json
 { "name": "calico-containerd-network", "cniVersion": "0.3.1", "plugins": [ { "type": "calico", "log_level": "info", "log_file_path": "/var/log/calico/cni/cni.log", "datastore_type": "etcdv3", "etcd_endpoints": "https://192.168.100.101:2379,https://192.168.100.102:2379,https://192.168.100.103:2379", "etcd_key_file": "/etc/calico/ssl/client.key", "etcd_cert_file": "/etc/calico/ssl/client.crt", "etcd_ca_cert_file": "/etc/calico/ssl/ca.crt", "nodename": "$HOSTNAME", "mtu": 0, "ipam": { "type": "calico-ipam" }, "container_settings": { "allow_ip_forwarding": true } }, { "type": "portmap", "snat": true, "capabilities": {"portMappings": true} }, { "type": "bandwidth", "capabilities": {"bandwidth": true} } ] } 

```