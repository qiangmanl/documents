```bash
mkdir $HOME/mosquitto
sudo chmod 777 -R $HOME/mosquitto
mkdir $HOME/mosquitto/config
cat >$HOME/mosquitto/config/mosquitto.conf <<EOF
persistence true
persistence_location /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log
allow_anonymous true
listener 1883
protocol mqtt

EOF

docker run -d --name mqtt -p 1883:1883    -v $HOME/mosquitto/:/mosquitto -v $HOME/mosquitto/data:/mosquitto/data    -v $HOME/mosquitto/log:/mosquitto/log \
-v $HOME/mosquitto/config/:/mosquitto/config eclipse-mosquitto
```
