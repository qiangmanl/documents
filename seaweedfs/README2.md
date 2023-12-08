# System enviroment

  ## Install
   
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

   
<!-- 
   ### install program
   ```bash
``    sudo apt install npm
    sudo npm install docsify
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
    lspci.

    
   ```

   >Mount
   ```bash
   sudo mount -t vfat /dev/sdc1 $mountpath
   ```

   >fdisk
   ```bash
   sudo fdisk /dev/sdc
   t  change a partition type
   a toggle a bootable flag
   ```

   ### directory
   ```bash
    tree
    #report file system disk space usage with "real size" format
    df -H

    #disk partition table list
    sudo fdisk -l
``   ``` -->
