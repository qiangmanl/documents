import time
import network
import socket

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
  



# while True:
#     time.sleep(1)

#     # Connect to the server
#     if response:
#         print(response)
#     else:
#         # Create a socket object
#         client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         # Connect to the server
#         client_socket.connect((host, port))
#           # Send the GET request
#           # Close the socket
#     response = client_socket.recv(4096).decode()
#     print(response)
# client_socket.close()




