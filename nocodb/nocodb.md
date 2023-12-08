```bash
docker run -d --name nocodb \
-v $HOME/testdata/nocodb:/usr/app/data/ \
-p 8080:8080 \
nocodb/nocodb:latest
```