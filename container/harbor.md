## harbor
>https://github.com/goharbor/harbor/releases/
>https://gitcode.net/mirrors/goharbor/harbor/-/releases


```
#harbor 证书
#私有根key
openssl genrsa -out ca.key 4096
#添加域名或者IP
openssl req -x509 -new -nodes -sha512 -days 365  -subj "/OU=habor/O=my servers/CN=qiangmanl.com"  -key ca.key  -out ca.crt

#再生成一个私有证书
openssl genrsa -out harbor_server.key 4096

#签名证书
 

cat > v3.ext <<-EOF
 authorityKeyIdentifier=keyid,issuer
 basicConstraints=CA:FALSE
 keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
 extendedKeyUsage = serverAuth 
 subjectAltName = @alt_names
 [alt_names]
 DNS.1=qiangmanl.com
 EOF
openssl x509 -req -sha512 -days 365 -extfile v3.ext -CA ca.crt -CAkey ca.key -CAcreateserial -in harbor_server.csr -out harbor_server.crt


#harbor.yml
  hostname : qiangmanl.com
  https:
port:443
  certificate: harbor_server.crt
  private_key: harbor_server.key


#安装

tar -zxvf harbor2.7.0-offline-installer.tgz 
cd habor 
ls
common     harbor.v2.7.0.tar.gz  harbor.yml.tmpl  install.sh  prepare
common.sh  harbor.yml            input            LICENSE

./prepare
./install

#docker 登录

docker login qiangmanl.com:8002
#添加证书路径 不成功待试
/etc/docker/certs.d/qiangmanl.com/

unsecurity login 
#add to /etc/docker/daemon.json
{
  "insecure-registries":["qiangmanl.com:8002"]
}

mkdir ~/foo
cd foo
make a Dockerfile then building...
docker build -f Dockerfile -t foo:v1 .
docker tag foo:v1 qiangmanl.com:8002/test/foo:v1
#project test in harbor before
docker push qiangmanl.com:8002/test/foo:v1



#containerd login
nerdctl login qiangmanl.com:8002 --insecure-registry

#containerd pull
nerdctl pull qiangmanl.com:8002/test/foo:v1 --insecure-registry


```