# System enviroment

  ## Preparation
   ### network
   >veth
   ```bash
    sudo  ip link add veth0 type veth peer name veth1
    sudo ip addr add 192.168.1.1/24 dev veth0
    sudo ip addr add 192.168.1.2/24 dev veth1
    ip link set veth0 up
    sudo ip link set veth0 up
    ping 192.168.1.1
    ping 192.168.1.2
    ip link show
   ```

   ### enviroment

   >add $HOME/.local/bin to $PATH
   ```bash
    vim /etc/enviroment
   ```

   ### apt china local source
   ```bash
    apt source /etc/apt/sources.list
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
   ```

   ### input method (sogou)
   >guide: https://shurufa.sogou.com/linux/guide
   >1.install fcitx and sogou

   ```bash
   sudo apt install fcitx
   sudo apt purge ibus
   #fcitx autostart with system run 
   sudo cp /usr/share/applications/fcitx.desktop /etc/xdg/autostart/
   #
   sudo apt install libqt5qml5 libqt5quick5 libqt5quickwidgets5 qml-module-qtquick2
   sudo apt install libgsettings-qt1
   ```
   >2.select Fcitx to input method system 
   >3.add sogou input method in fcitx configure
   >4.restart system
   ### install program
   ```bash
    sudo apt install npm
    sudo npm install docsify-cli -g
    sudo apt install curl


    #miniconda
    #download minconda and installed
    #auto deactivate base env
    conda config --set auto_activate_base false

    #google chrome
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb 
    #run 
    google-chrome

   ```

  ## System command

   ### device
   >Print Hardware lister 
   ```bash
    lshw
   ```

   >Print PCI devices lister 
   ```bash
    lspci
   ```

   >Mount
   ```bash
   sudo mount -t vfat /dev/sdc1 $mountpath
   ```

   >Disk Device
   ```bash
   sudo fdisk /dev/sdc
   t  change a partition type
   a toggle a bootable flag
   ```
   >Print a system service journal
   ```bash
   journalctl -n 20 --no-pager --user --unit containerd.service
   ```
   >format a partition in a device
   ```bash
    sudo mkfs.ext4 /dev/sdb2
   ```
   >lsblk block mounting status
   ```bash
   lsblk
   ```

   ### directory
   ```bash
    tree
    #report file system disk space usage with "real size" format
    df -H
    #disk partition table list
    sudo fdisk -l
   ```

# Application
  ## edk2
  >enviroment:ubuntu20.04
  >resource: <https://github.com/tianocore/edk2/>
  ### build
  >if gcc >=11
  git clone https://github.com/google/brotli/tree/f4153a09f87cbb9c826d8fc12c74642bb2d879ea
  >else
  git clone https://github.com/google/brotli
  >change value  TARGET_ARCH = X64,TOOL_CHAIN_TAG = GCC5 to Conf/target.txt
  mv brotli to directory where "make -C BaseTools" entering directory but no such file or directory
  then run "make -C BaseTools" again

  ```bash
  sudo apt install build-essential iasl git  nasm  python-is-python3
  sudo apt-get install uuid-dev xorg-dev
  git clone https://github.com/tianocore/edk2/
  cd edk2
  make -C BaseTools/
  source edksetup.sh 
  build -v --debug 0
  
  ```
  ### run
  ```bash
  ./Build/EmulatorX64/DEBUG_GCC5/X64/Host 
  ```
  ## npm
   >update node
   ```bash
     npm install -g n 
     n stable
   ```
   #make .npmrc audit false for silent install audit warning
   ```bash
    npm set audit false
   ```
  ## conda
   >auto deactivate base env
   ```bash
    conda config --set auto_activate_base false
   ```

  ## docsify

   >install
   ```bash
    sudo npm install docsify-cli -g 
   ```

   >initialize project
   ```bash
    docsify init ./project
   ```

   >add sidebar 
   ```bash
    docsify generate ./project
   ```
   >run project 
   ```bash
    docsify serve ./project
   ```

  ## Wireshark 

   >install
   ```bash
    sudo apt install wireshark-qt
   ```

# Network

  ## Nmap

  > 

  

  ```bash
  # fast scan to search who's host is up 
  nmap -sP 192.168.99.0/24
  # fast scan to singe host
  nmap -sP  192.168.99.202

  #
  ```

  ## Net-snmp
  >NMS（Network Management System)
  >Agent
  >MIB（Management Information Base)
  >SNMP网络架构由三部分组成：NMS、Agent和MIB。
  >NMS（Network Management System，网络管理系统）是SNMP网络的管理者，能够提供友好的人机交互界面，方便网络管理员完成大多数的网络管理工作。
  >Agent是SNMP网络的被管理者，负责接收、处理来自NMS的SNMP报文。在某些情况下，如接口状态发生改变时，Agent也会主动向NMS发送告警信息。
  >MIB（Management Information Base，管理信息库）是被管理对象的集合。NMS管理设备的时候，通常会关注设备的一些参数，比如接口状态、CPU利用率等，这些参数就是被管理对象，在MIB中>称为节点。每个Agent都有自己的MIB。MIB定义了节点之间的层次关系以及对象的一系列属性，比如对象的名称、访问权限和数据类型等。被管理设备都有自己的MIB文件，在NMS上编译这些MIB文件，>就能生成该设备的MIB。NMS根据访问权限对MIB节点进行读/写操作，从而实现对Agent的管理。

  #http://www.net-snmp.org/download.html
  >Install
  ```bash
  sudo apt-get install libperl-dev
  cd net-snmp*
  ./configure --prefix=/usr/local/net-snmp
  sudo make 
  sudo make install 
  sudo systemctl unmask snmpd
  snmpget --version

  ```