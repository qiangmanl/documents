```yaml

version: '3.1'

networks:
  network-zabbix:
    driver: bridge

services:
  mysql:
    container_name: mysql
    image: mysql:5.7
    networks:
      - network-zabbix
    volumes:
      - './zabbix/mysql:/var/lib/data'
    environment:
      - MYSQL_ROOT_PASSWORD=carryontech
      - MYSQL_DATABASE=zabbix
      - MYSQL_USER=zabbix
      - MYSQL_PASSWORD=carryontech

  zabbix-server:
    container_name: zabbix-server
    image: zabbix/zabbix-server-mysql:ubuntu-5.0.1
    networks:
      - network-zabbix
    links:
      - mysql
    restart: always
    ports:
      - '10051:10051'
    volumes:
      - './zabbix/alertscripts:/usr/lib/zabbix/alertscripts'
    environment:
      - DB_SERVER_HOST=mysql
      - MYSQL_DATABASE=zabbix
      - MYSQL_USER=zabbix
      - MYSQL_PASSWORD=carryontech
    depends_on:
      - mysql

  zabbix-frontend:
    container_name: zabbix-frontend
    image: zabbix/zabbix-web-apache-mysql:ubuntu-5.0.1
    networks:
      - network-zabbix
    links:
      - mysql
    restart: always
    ports:
      - '8001:8080'
      - '443:8443'
    environment:
      - DB_SERVER_HOST=mysql
      - MYSQL_DATABASE=zabbix
      - MYSQL_USER=zabbix
      - MYSQL_PASSWORD=carryontech
      - PHP_TZ=America/Sao_Paulo
    depends_on:
      - mysql
      - zabbix-server
```
