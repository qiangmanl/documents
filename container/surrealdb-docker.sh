mkdir -p surrealdb
cd surrealdb
cat >Dockerfile <<EOF
    FROM gcr.io/distroless/cc:latest

    ARG TARGETARCH

    ADD $TARGETARCH/surreal /

    ENTRYPOINT ["/surreal"]
EOF


docker container create --name surrealdb surrealdb/surrealdb:latest start -h

docker logs surrealdb
# surreal-start 
# Start the database server

# USAGE:
#     surreal start [OPTIONS] [--] [path]

# ARGS:
#     <path>    Database path used for storing data [env: DB_PATH=] [default: memory]

# OPTIONS:
#         --addr <addr>          The allowed networks for master authentication [env: ADDR=] [default:
#                                127.0.0.1/32]
#     -b, --bind <bind>          The hostname or ip address to listen for connections on [env: BIND=]
#                                [default: 0.0.0.0:8000]
#     -h, --help                 Print help information
#     -k, --key <key>            Encryption key to use for on-disk encryption [env: KEY=]
#         --kvs-ca <kvs-ca>      Path to the CA file used when connecting to the remote KV store [env:
#                                KVS_CA=]
#         --kvs-crt <kvs-crt>    Path to the certificate file used when connecting to the remote KV
#                                store [env: KVS_CRT=]
#         --kvs-key <kvs-key>    Path to the private key file used when connecting to the remote KV
#                                store [env: KVS_KEY=]
#     -l, --log <log>            The logging level for the database server [env: LOG=] [default: info]
#                                [possible values: warn, info, debug, trace, full]
#     -p, --pass <pass>          The master password for the database [env: PASS=]
#     -s, --strict               Whether strict mode is enabled on this database instance [env:
#                                STRICT=]
#     -u, --user <user>          The master username for the database [env: USER=] [default: root]
#         --web-crt <web-crt>    Path to the certificate file for encrypted client connections [env:
#                                WEB_CRT=]
#         --web-key <web-key>    Path to the private key file for encrypted client connections [env:
#                                WEB_KEY=]

docker container rm  surrealdb

docker container create --name surrealdb -p 8000:8000 surrealdb/surrealdb:latest  start \
 -u yang -p whoisyang /home/data
docker container create --name surrealdb -p 8000:8000 -v /surrealhome:/home surrealdb/surrealdb:latest\
  start  -u yan -p iamyan "file:///home/data.db"

  
DATA="INFO FOR DB;"
curl --request POST \
	--header "Accept: application/json" \
	--user "yang:whoisyang" \
	--data "${DATA}" \
    --header "NS: test" \
	--header "DB: test" \
	http://localhost:5001/sql



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

    

DATA="CREATE author:johna SET
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
