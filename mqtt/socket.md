```python
#get 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr=socket.getaddrinfo("192.168.10.254",80)[0][-1]
sock.connect(addr)
sock.close()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(addr)
request = f"GET / HTTP/1.1\r\nHost: {addr[0]}\r\n\r\n"
sock.send(request.encode())
response = sock.recv(4096).decode()
data = json.loads(response.split("\r\n")[-1])
```

```python
import time
json_data = '{"message": "Hello, MQTT!"}'
server_address="192.168.10.254"
server_port=8200
addr = socket.getaddrinfo(server_address, server_port)[0][-1]
#while
request = (
    "POST /publish HTTP/1.1\r\n"
    "Host: {}:{}\r\n"
    "Content-Type: application/json\r\n"
    "Content-Length: {}\r\n"
    "\r\n"
    "{}"
).format(server_address, server_port, len(json_data), json_data)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(addr)
sock.send(request.encode())
response_data = b""
sock.settimeout(5)
# response = sock.recv(4096)

while True:
    chunk = sock.recv(4096)
    # chunk2 = sock.recv(4096)
    if not chunk:
        break
    response_data += chunk



print(response_data.decode())
sock.close()
#end while
```
