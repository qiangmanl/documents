docker run -d \
   --name navidrome \
   --restart=unless-stopped \
   --user $(id -u):$(id -g) \
   -e ND_LOGLEVEL=info \
   -e ND_LASTFM_LANGUAGE: zh\
   -v /home/yang/navidrome/music:/music \
   -v /home/yang/navidrome/data:/data \
   -v /home/yang/navidrome/app:/app\
   -p 4533:4533 deluan/navidrome:latest
