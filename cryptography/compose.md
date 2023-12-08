  # Compose

   ## yaml 
   >example
   ```yaml
  version: '3'
  services: 
    redis:
      container_name: redis-container
      image: redis:7.0.0
      ports:
        - 6379:6379
      volumes:
        - "${REDIS_LOCAL_DIR}/redis.conf:/etc/redis/redis.conf"
        - "${REDIS_LOCAL_DIR}/logs:/usr/local/redis/logs"
        - "${REDIS_LOCAL_DIR}/data:/data"
        - "${REDIS_LOCAL_DIR}/home:/home"
      command: [ "redis-server", "/etc/redis/redis.conf" ]
      #privileged: true
      restart: always
   ```
   >.env
   ```bash
   REDIS_LOCAL_DIR=./redis-local
   ```
   

