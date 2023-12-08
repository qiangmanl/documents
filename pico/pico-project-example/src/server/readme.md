```bash
pip install -r requirement.txt 
docker container create --rm --name surreal_for_test -p 6666:8000 surrealdb/surrealdb:latest  start \
 -u sft -p sft 
docker start surreal_for_test


docker stop surreal_for_test
 python app.py

#
#get relay
http://192.168.99.214:7000/relayTasks?device=a
#do relay
http://192.168.99.214:7000/relayDoTask?device=a

curl -X POST -H "Content-Type: application/json" -d '{"channel":1,"switch":"ON", "device":"a"}' http://192.168.99.214:7000/relayTasks

```