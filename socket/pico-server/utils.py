import time
import network


def scan_wifi():
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  print(wlan.scan())


def connect_wifi(ssid, password):

  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  try:
      wlan.disconnect()
  except:
      pass
  wlan.connect(ssid, password)
  
  # Wait for connect or fail
  max_wait = 10
  while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
      break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
  
  # Handle connection error
  if wlan.status() != 3:
    raise RuntimeError('network connection failed')
  else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    return True
  







    

def parse_request(request):

    request_lines = request.split('\r\n')
    data = ""
    for line in request_lines:
        if line.startswith('Content-Length'):
            content_length = int(line.split(':')[1].strip())
        if line == '':
            data = request_lines[-1]
    return data

def handle_connection(client_socket):

    request_data = client_socket.recv(1024).decode()

    data = parse_request(request_data)
    
    #handle post
    print("Received data:", data)

    response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, World!'
    client_socket.sendall(response.encode())

    client_socket.close()





