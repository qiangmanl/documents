## Containerd
  >
  >

   ### install
   ```bash
    sudo apt install containerd
    ctr version
    sudo mkdir /etc/containerd
    sudo containerd config default > config.toml 
    cat config.toml 
    sudo mv config.toml /etc/containerd
    cat /etc/containerd/config.toml
    sudo ctr plugin ls
   ```
   ####
   ```bash
   curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
   yum install wget jq psmisc vim net-tools telnet yum-utils device-mapper-persistent-data lvm2 git -y
   yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
   yum install containerd
  containerd config default >/etc/containerd/config.toml
  systemctl enable containerd
  systemctl start containerd
   ```
   ### command
   >pull
   ```bash
    #pull image resource
    ctr images pull docker.io/chrislusf/seaweedfs:3.20 

   ```
   >mount (un)mount have only spacified the ctr)
   ```bash
   mkdir /foo
   ctr -n k8s.io  images mount docker.io/library/nginx:alpine /foo
   ctr images mount docker.io/library/nginx:alpine /foo
   ctr  -n k8s.io images unmount /foo
   ctr unmount /foo
   ```

   >namespace
   ```bash
    ctr -n k8s.io container  ls
    #print namespace list
    ctr namespace ls 
   ```

   > image 
   ```bash
    #  image ls 
    ctr -n k8s.io  images ls
    # mount
    ctr -n k8s.io  images mount docker.io/library/nginx:alpine /foo
    nerdctl -n k8s.io container --name create docker.io/chrislusf/seaweedfs  swfs


   ```
   >container
   ```bash
  # 创建容器时可以更改ID,不是像nerdctl那样tag a name但在nerdctl 下没什么用
  #  刚创建的container  通过ps -a 和ctr container ls 查看，tasks则不能

   ctr -n k8s.io container create docker.io/library/nginx:alpine nginx
   ctr -n server container create docker.io/coredns/coredns:latest coredns
   #  nerdctl
   nerdctl --namespace k8s.io container create --net bridge docker.io/library/nginx:alpine  
  nerdctl --namespace k8s.io container create -p 8011:80 --name nginx1  --ip 10.4.0.111 docker.io/library/nginx:alpine:latest nginx
  nerdctl -n k8s.io container create -p 8011:80 --name nginx2  --net bridge docker.io/library/nginx:latest 
  # nerdctl -n k8s.io container create -p 8011:80 --name nginx94  --ip 10.4.0.94 docker.io/library/nginx:latest 'nginx -g daemon off'
  
  nerdctl create --name ha \
   --net bridge \
   --privileged \
   --env TZ=Asia/Shanghai \
   -p 8123:8123 \
   --mount type=bind,src=/home/yang/homeassistant,dst=/config \
   ghcr.io/home-assistant/home-assistant:stable 
  # paralleled mount  host \data1 to container /home 
  nerdctl -n k8s.io container  create --mount dst=/home,src=\data1 ...


  
  nerdctl -n k8s.io start nginx94
  nerdctl -n k8s.io ps --no-trunc
  nerdctl -n k8s.io  stop nginx94
  nerdctl -n k8s.io rm  nginx94
   #start a container to task
   ctr -n k8s.io tasks start -d nginx
   #  nerdctl start a container to task 
  nerdctl   --namespace k8s.io   run -d --net bridge nginx foo
  nerdctl  --namespace k8s.io   run -d nginx 

  #  restart
   ctr -n k8s.io tasks kill nginx
   ctr -n k8s.io tasks rm nginx
   ctr -n k8s.io tasks start -d nginx
  #ps
   nerdctl -n k8s.io ps
   nerdctl -n k8s.io container ls
   ctr -n k8s.io tasks ls
  # ps -a
   ctr -n k8s.io c ls 


   ctr -n k8s.io task  exec --exec-id 1 -t nginx sh 

   ```
   >metrics
   ```bash
   ctr t metrics nginx
   ```

   >network
```bash

   nerdctl network create foo2
   # none net ===no ip
   nerdctl run -d --name * --net none 
   #
   nerdctl * --net host
   ```
   >network cni bridge ip 分配问题
   ```bash
   #to known rm all tasks 
   ctr -n k8s.io tasks ls
   cat /etc/cni/net.d/nerdctl-bridge.conflist 
  #  指定 cni
   nerdctl   --namespace k8s.io   run -d --net bridge nginx
  # 指定 cni ip 
   nerdctl   --namespace k8s.io   run -d --net bridge --ip 10.4.0.212 nginx
   #del bridge link
   ifconfig  nerdctl0 down 
   ip link del nerdctl0
  ```

   

   >example
   ```bash
  #  search
   docker search seaweedfs
    # NAME                    DESCRIPTION                       STARS     OFFICIAL   AUTOMATED
    # chrislusf/seaweedfs     official seaweedfs docker builds   32                   [OK]
  
  # create images
  #  pull
   nerdctl pull --namespace k8s.io docker.io/chrislusf/seaweedfs:latest
   ctr -n k8s.io  images pull docker.io/library/nginx:alpine
  
  #  from docker export 
  nerdctl  --namespace k8s.io image   save -o f.tar docker.io/library/nginx:latest
  nerdctl  image load -i f.tar
  
  # ls images
  nerdctl --namespace k8s.io images
  # REPOSITORY             TAG       IMAGE ID        CREATED           PLATFORM       SIZE         BLOB SIZE
  # chrislusf/seaweedfs    3.20      511889a4ff3c    16 minutes ago    linux/amd64    85.0 MiB     39.1 MiB
  #swfs is a COMMAND postfix changed "/docker-entrypoint.sh swsf" in container command

  # create container 
  nerdctl -n k8s.io container create --net bridge docker.io/chrislusf/seaweedfs:latest  nginx

  ```

