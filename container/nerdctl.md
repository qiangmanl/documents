  ## Nerdctl
   ### install
   ```bash
    #download new version crictl from https://github.com/kubernetes-sigs/cri-tools/releases 
    #archive and mv crictl to local bin.

    #set containered endpoint  
    #download nerdctl from https://github.com/containerd/nerdctl/ and archive
    sudo apt install rootlesskit
    mv containerd-rootless.sh  ~/.local/bin/  
    ./containerd-rootless-setuptool.sh install
    mv nerdctl ~/.local/bin/


    #install cni network plugin
    #download cni plugins from https://github.com/containernetworking/plugins/releases
    #mkdir previous path if not exist
    sudo mkdir -p /opt/cni/bin
    tar xvf cni-plugins-linux-amd64-{{version}}.tgz -C /opt/cni/bin/
    sudo su
    #nerdctl
   ```
   #### centos
   ```bash
   wget https://ghproxy.com/https://github.com/containerd/nerdctl/releases/download/v1.1.0/nerdctl-full-1.1.0-linux-amd64.tar.gz
   tar zxvf  nerdctl-full-1.1.0-linux-amd64.tar.gz
   mv bin/* /usr/local/bin/
   mv lib/* /usr/local/lib/
   mv libexec/* /usr/local/libexec/
   mv share/* /usr/local/share/
   ``` 
   
   ### command
   >coinainer  
   >!!!nerdctr can not list the container when ctr commond create a container.
   ```bash
   nerdctl -n k8s.io container create docker.io/library/nginx:alpine nginx
   ctr -n k8s.io task  exec --exec-id 1 -t nginx sh 
   ```
   >namespace
   ```bash
   nerdctl -n k8s.io container create docker.io/library/nginx:alpine nginx
   nerdctl -n k8s.io  pull docker.io/library/nginx:alpine
   nerdctl -n k8s.io  images 
   nerdctl -n k8s.io  rmi 455
   ```
   ```bash
    sudo nerdctl network ls 
    #run a container in compose
    sudo nerdctl compose -f ./examples/compose-wordpress/docker-compose.yaml up

    #run a container
    nerdctl -n k8s.io container  -n k8s.io  run  nginx
    # a accomplish task create.
    nerdctl   --namespace k8s.io run -d -p 8011:80 --name nginx1  --ip 10.4.0.212 nginx
  nerdctl  run -d -p 8011:80 --name nginx1  --ip 10.0.0.212 nginx
    #ps
    nerdctl -n k8s.io ps
    nerdctl -n k8s.io container ls

    #pull image
    nerdctl pull docker.io/chrislusf/seaweedfs:3.20 
    #
    sudo nerdctl exec  -it $container /bin/bash
   ```
   >images

   ```bash
    #
    ctr inspect docker.io/chrislusf/seaweedfs:3.20 
    #nerdctl commit  生成新的镜像包含容器数据，但在镜像中的路径中未必能查找到。可见数据和镜像是分离的
    nerdctl commit $image $newimage
   ```
