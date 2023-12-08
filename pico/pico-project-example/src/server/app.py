
from server import server


if server.protocol == "http":
    from server.routes.http import *
    server.add_http_route(hello,"/hello")
    server.add_http_route(listen_relay_task, "/relayTasks", methods=["GET", "POST"])
    server.add_http_route(relay_do_task, "/relayDoTask",methods=["GET"])

    
if __name__ == "__main__":
    server.run(host='0.0.0.0', port=7000)