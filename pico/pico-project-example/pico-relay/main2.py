import socket
import time
import json
from const import DEVICE, HOST, PORT, SSID, WIFI_PSWD,DO_URI
from utils import  connect_wifi
from relay import do_response,channels


#get 
import json
addr=socket.getaddrinfo("192.168.10.254",80)[0][-1]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(addr)
sock.close()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(addr)
request = f"GET / HTTP/1.1\r\nHost: {addr[0]}\r\n\r\n"
sock.send(request.encode())
response = sock.recv(4096).decode()
data = json.loads(response.split("\r\n")[-1])








curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello, MQTT!"}' http://localhost:8200/publish

if __name__ == "__main__":
    if connect_wifi(SSID, WIFI_PSWD):
    # Create a socket object
        while True:
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # Connect to the server
                client_socket.connect((HOST, PORT))

                # Send the GET request
                request = f"GET /{DO_URI}?device={DEVICE} HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
                client_socket.send(request.encode())
                # Receive and print the response
                response = client_socket.recv(4096).decode()
                data = json.loads(response.split("\r\n")[-1])
                print(data)
                if (data["device"] == DEVICE) and (data["ch"] in channels.keys()):
                    # print(response) =>{"ch":3,"switch":"ON","device":"a"}
                    if data["act"]  == 0:
                        do_response(channel=data["ch"], switch=data["switch"])
 #                       print(True)
                # Close the socket
                client_socket.close()

            except Exception as e:
                print("An error occurred:", str(e))
                client_socket.close()
            # Delay for 2 seconds
            time.sleep(2)
