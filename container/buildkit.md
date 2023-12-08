# buildkit

  ## Install
   
   ```bash
   wget https://github.com/moby/buildkit/releases/download/$version/buildkit-$version.linux-amd64.tar.gz

   tar  ***
   #cd buildkit filepath
   mv * pathtopath/bin 

   #create buildkitd service
   #/usr/lib/systemd/system/buildkitd.service
   [Unit]
   Description=BuildKit
   Requires=buildkit.socket
   After=buildkit.socket
   Documentation=https://github.com/moby/buildkit
   [Service]
   Type=notify
   ExecStart=/usr/local/bin/buildkitd --addr fd:// --oci-worker=false --containerd-worker=true
   [Install]
   WantedBy=multi-user.target


   #/usr/lib/systemd/system/buildkit.socket
   [Unit]
   Description=BuildKit
   Documentation=https://github.com/moby/buildkit
   [Socket]
   ListenStream=%t/buildkit/buildkitd.sock
   SocketMode=0660
   [Install]
    WantedBy=sockets.target
   
   #
   sudo systemctl start buildkit
   ```
   >registry的帐号密码配置在 ~/.docker/config.json 文件中 , 沿用了Docker的配置,虽然我们并没有装Docker
  ```bash
  {
          "auths": {
                  "docker.io": {
                          "auth": "c2hpb3lpbTpAdGhlc2t5eWV0ODg="
                  }
          }
  }
  #build and push
  buildctl build \
--frontend=dockerfile.v0 \
    --local context=. \
    --local dockerfile=. \
    --output type=image,name=docker.io/username/image:tag,push=true
   ```
   buildctl build     --frontend=dockerfile.v0     --local context=.     --local dockerfile=.     --output type=image,name=docker.io/username/image:tag 
