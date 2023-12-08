import socket
from const import HOST, PORT, SSID, PASSWD
from utils import handle_connection , connect_wifi

def run_server(host, port):


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((HOST, PORT))

    server_socket.listen(1)
    print('Listening on {}:{}'.format(HOST, PORT))

    while True:

        client_socket, client_address = server_socket.accept()
        print('Accepted connection from {}:{}'.format(*client_address))
        handle_connection(client_socket)

if __name__ == "__main__":
    if connect_wifi(SSID, PASSWD):
        run_server(HOST, PORT)