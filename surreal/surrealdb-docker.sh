mkdir -p surrealdb
cd surrealdb
cat >Dockerfile <<EOF
    FROM gcr.io/distroless/cc:latest

    ARG TARGETARCH

    ADD $TARGETARCH/surreal /

    ENTRYPOINT ["/surreal"]
EOF


#docker container create --name surrealdb surrealdb/surrealdb:1.0.0 start -h

docker logs surrealdb


docker container rm  surrealdb
#memery
docker container create --name surrealdb -p 8000:8000 surrealdb/surrealdb:latest  start \
 -u yang -p whoisyang 
# local 
docker container create --name surrealdb -p 8000:8000 -v /surrealhome:/home surrealdb/surrealdb:latest\
  start  -u yan -p iamyan "file:///home/data.db"

  
DATA="INFO FOR DB;"
curl --request POST \
	--header "Accept: application/json" \
	--user "yan:iamyan" \
	--data "${DATA}" \
    --header "NS: test" \
	--header "DB: test" \
	http://localhost:8000/sql



DATA="CREATE account SET
	name = 'ACME Inc',
	created_at = time::now();"

curl -k -L -s --compressed POST \
	--header "Accept: application/json" \
	--header "NS: test" \
	--header "DB: test" \
	--user "yan:iamyan" \
	--data "${DATA}" \
	http://localhost:8000/sql

DATA="CREATE author:\"johna dsahjhdf  dfshhs hdh adsh hkhds fhhfdfsddfag g\" SET
	first = 'John',
	last = 'Adams',
	age = 29,
	admin = true,
signup_at = time::now();"

DATA="CREATE author:"johna" SET
	name.first = 'John',
	name.last = 'Adams',
	name.full = string::join(' ', name.first, name.last),
	age = 29,
	admin = true,
	signup_at = time::now();"

curl -k -L -s --compressed POST \
	--header "Accept: application/json" \
	--header "NS: test" \
	--header "DB: test" \
	--user "yang:whoisyang" \
	--data "${DATA}" \
	http://localhost:8000/sql




# Querying data
# SELECT * FROM article;
DATA="SELECT * FROM author;"
curl -k -L -s --compressed POST \
	--header "Accept: application/json" \
	--header "NS: test" \
	--header "DB: test" \
	--user "yang:whoisyang" \
	--data "${DATA}" \
	http://localhost:8000/sql


data="CREATE ducuments:2  SET
    ask = '关闭swap(close swap)',
    result = 'free -m |grep -i swap',
    update = time::now();"
	
curl --request POST \
	--header "Accept: application/json" \
    --header "NS: {namespace}" \
	--header "DB: mysearch-db" \
	--user "yang:iamyang" \
	--data "${data}" \
	http://localhost:7698/sql

data="SELECT * FROM ducuments;"






docker stop surrealdb;docker rm surrealdb
