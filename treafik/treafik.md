```bash



docker network create --driver bridge --subnet 172.100.0.0/16 treafik_network 


cat >traefik.toml<<EOF
[entryPoints]
  [entryPoints.http]
      address = ":80"
      [entryPoints.http.http.redirections.entryPoint]
          to = "https"
          scheme = "https"
  [entryPoints.https]
      address = ":443"
 
[providers]
  [providers.docker]
    network = "traefik"
EOF

docker run -d   -p 80:80   -p 443:443  -p 8080:8080  -v $PWD/traefik.toml:/traefik.toml   -v /var/run/docker.sock:/var/run/docker.sock  --name traefik   --network treafik_network   traefik:v2.6  --api.insecure=true --providers.docker

docker run -d   --label "traefik.http.routers.nginx.rule=Host(`ihotel.lo`)"   --name nginx   --network treafik_network   nginx:latest
```


