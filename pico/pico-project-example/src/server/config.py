#protocal : "http" || "ws"

test_config = {
    "server" : {
        "appname":"test-pico",
        "protocol": "http"
    },
    "sql":{
        "name" :"surreal",
        "name_space": "test",
        "data_base" :"test",
        "addr" :"http://localhost:6666/sql",
        "username":"sft",
        "password" :"sft" 
        #more sureal config
    },
    "devices":["a"]
}

server_config = test_config["server"]
sql_config = test_config["sql"]
devices = test_config["devices"]
