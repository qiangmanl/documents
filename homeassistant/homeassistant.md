
```bash
  nerdctl create --name dvsmnt \
   --restart always \
   --net bridge \
   --privileged \
   --env TZ=Asia/Shanghai \
   -p 8901:8123 \
   --mount type=bind,src="$HOME"/backup/homeassistant/devices_monitor_config,dst=/config \
   ghcr.io/home-assistant/home-assistant:stable 


  nerdctl create --name rmsmnt \
   --restart always \
   --net bridge \
   --privileged \
   --env TZ=Asia/Shanghai \
   -p 8902:8123 \
   --mount type=bind,src="$HOME"/backup/homeassistant/rooms_monitor_config,dst=/config \
   ghcr.io/home-assistant/home-assistant:stable 
   
  nerdctl create --name nwksmnt \
   --restart always \
   --net bridge \
   --privileged \
   --env TZ=Asia/Shanghai \
   -p 8903:8123 \
   --mount type=bind,src="$HOME"/backup/homeassistant/networks_monitor_config,dst=/config \
   ghcr.io/home-assistant/home-assistant:stable 
   

  nerdctl create --name mtmnt \
   --restart always \
   --net bridge \
   --privileged \
   --env TZ=Asia/Shanghai \
   -p 8904:8123 \
   --mount type=bind,src="$HOME"/backup/homeassistant/maintain_monitor_config,dst=/config \
   ghcr.io/home-assistant/home-assistant:stable 
   

   
   nerdctl start nwksmnt
   nerdctl start dvsmnt
   nerdctl start rmsmnt

```



```yaml
  binary_sensor:
    - platform: command_line
      unique_id : ffdsfdsad
      name: test_ui
      
      
      command: "echo 'arp -d 192.168.99.12;ping -c 1 192.168.99.12;arp -n |grep 192.168.99.12 | grep -i b1:3c:01 > /dev/null && echo 1 || echo 0'>/config/1"
      payload_on: 1
      payload_off: 0
      scan_interval: 30
      
      

switch:
  - platform: command_line
    unique_id : a
    switches:
      kitchen_light:
        command_on: "curl -X POST -H \"Content-Type: application/json\" -d '{\"channel\":1,\"switch\":\"ON\", \"device\":\"a\"}' http://192.168.99.214:7000/relayTasks"
        command_off: "curl -X POST -H \"Content-Type: application/json\" -d '{\"channel\":1,\"switch\":\"OFF\", \"device\":\"a\"}' http://192.168.99.214:7000/relayTasks"

      
```
