##shc 编译成二进制 

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

dpkg -i ./google-chrome-stable_current_amd64.deb

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 
chmod a+x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh

# conda config --set auto_activate_base false
# You can undo this by running `conda init --reverse $SHELL`? [yes|no]
# [no] >>> yes

conda  create -n test python=3.11
cp ~/.bashrc ~/.bashrc_bak
echo "alias acttest='conda activate test'">>~/.bashrc
echo "alias deactenv='conda activate test'">>~/.bashrc


#
sudo apt install git

#pip 
rm -rf ~/.pip
mkdir ~/.pip
cat >~/.pip/pip.conf<<EOF
[global] 
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn 
EOF



#sougou
sudo apt install fcitx
sudo apt install libqt5qml5 libqt5quick5 libqt5quickwidgets5 qml-module-qtquick2
sudo apt install libgsettings-qt1
sudo cp /usr/share/applications/fcitx.desktop /etc/xdg/autostart/
sudo apt purge ibus
#dpkg -i  ...
#select input method system:fcitx 

#

sudo apt-get install build-essential libatlas-base-dev gfortran



#after docker installed
sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo systemctl restartdocker 
sudo systemctl restart docker 
newgrp - docker





