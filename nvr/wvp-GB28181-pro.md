```bash
sudo apt-get install -y openjdk-11-jre
sudo apt-get install -y maven

git clone https://gitee.com/pan648540858/wvp-GB28181-pro.git
cd wvp-GB28181-pro/web_src/
npm --registry=https://registry.npmmirror.com install
npm run build
cd ..
mvn package
mvn package -P war
cd target/
mv ../src/main/resources/application-dev.yml application.yml 
java -jar wvp-pro-*.jar --spring.config.location=application.yml

cd ..
ls
docker run -d --name redis -p 6379:6379 --restart=always redis:7.0.2 --requirepass "www.coderyj.com"
docker run -d  -v /coderyj/data:/var/lib/mysql --privileged --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=coderyj --restart=always mysql:5.7.25 



sudo apt-get install libsrtp2-dev
git clone --depth 1 https://gitee.com/xia-chu/ZLMediaKit
cd ZLMediaKit
#千万不要忘记执行这句命令
git submodule update --init
mkdir build
cd build
cmake .. -DENABLE_WEBRTC=true  -DOPENSSL_ROOT_DIR=/usr/local/openssl  -DOPENSSL_LIBRARIES=/usr/local/openssl/lib
cmake --build . --target MediaServer

find ./ -name MediaServer
sudo lsof -i :$PORT


docker exec -i mysql  mysql -u root -pcoderyj < /coderyj/data/init.sql
```


