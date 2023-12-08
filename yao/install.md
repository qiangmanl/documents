docker run -d --name yao -v $HOME/testdata/yaoapp:/data/app -p 5099:5099 yaoapp/yao:0.10.3-amd64-dev

docker run -d -p 3308:3306 --restart unless-stopped -e MYSQL_PASSWORD=123456 yaoapp/mysql:8.0-amd64



docker exec -it yao /bin/bash

yao run xiang.main.Inspect

yao start
