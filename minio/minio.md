```bash
docker network create -d bridge --subnet 172.30.0.0/24 --gateway 172.30.0.1 minio-network

docker run  -d --restart always -p 8500:9000    -p 8600:9090    --name minio1    --network minio-network    --ip 172.30.0.2    -v "$HOME"/minio/data1:/data1    -e "MINIO_ROOT_USER=miniouser"    -e "MINIO_ROOT_PASSWORD=miniopassword"    docker.io/minio/minio:latest server http://172.30.0.2/data1 http://172.30.0.3/data1 http://172.30.0.4/data1 http://172.30.0.5/data1 --console-address ":9090"

docker run  -d  --restart always   -p 8501:9000    -p 8601:9090    --name minio2    --network minio-network    --ip 172.30.0.3   -v "$HOME"/minio/data2:/data1    -e "MINIO_ROOT_USER=miniouser"    -e "MINIO_ROOT_PASSWORD=miniopassword"    docker.io/minio/minio:latest server http://172.30.0.2/data1 http://172.30.0.3/data1 http://172.30.0.4/data1 http://172.30.0.5/data1 --console-address ":9090"

 docker run  -d  --restart always  -p 8502:9000    -p 8602:9090    --name minio3    --network minio-network    --ip 172.30.0.4    -v "$HOME"/minio/data3:/data1    -e "MINIO_ROOT_USER=miniouser"    -e "MINIO_ROOT_PASSWORD=miniopassword"    docker.io/minio/minio:latest server http://172.30.0.2/data1 http://172.30.0.3/data1 http://172.30.0.4/data1 http://172.30.0.5/data1 --console-address ":9090"

docker run  -d  --restart always   -p 8503:9000    -p 8603:9090    --name minio4    --network minio-network    --ip 172.30.0.5    -v "$HOME"/minio/data4:/data1    -e "MINIO_ROOT_USER=miniouser"    -e "MINIO_ROOT_PASSWORD=miniopassword"    docker.io/minio/minio:latest server http://172.30.0.2/data1 http://172.30.0.3/data1 http://172.30.0.4/data1 http://172.30.0.5/data1 --console-address ":9090"



set_policy_for_bucket.py

wget https://dl.min.io/client/mc/release/linux-amd64/mc

mc alias set myminio http://127.0.0.1:8500 miniouser  miniopassword
mc alias set myminio http://127.0.0.1:8500 m11 m1111111

#policy set unset
mc admin policy set myminio testpolicy group=testgroup
mc admin policy unset myminio testpolicy group=testgroup
mc admin info myminio
# echo m11:m1111111 >$HOME/.miniopw2
# Create Access Key from minio console to .miniopw
chmod 600 /home/yang/.miniopw
chmod 600 /home/yang/.miniopw2
#一定要关掉代理
sudo sed -i 's/#user_allow_other/user_allow_other/g' /etc/fuse.conf
#test /mnt
s3fs -o passwd_file=$HOME/.miniopw -o url=http://127.0.0.1:8500 -o nonempty  -o allow_other -o no_check_certificate -o use_path_request_style -o umask=000 test  /mnt/s3 -d -d -f -o f2 -o curldbg

s3fs -o passwd_file=$HOME/.miniopw -o url=http://127.0.0.1:8500 -o nonempty  -o no_check_certificate -o use_path_request_style -o umask=000 test  /mnt/s3 -d -d -f -o f2 -o curldbg
```





