import socket

def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's port
    server_address = ('localhost', 65432)
    print('Connecting to {} port {}'.format(*server_address))
    client_socket.connect(server_address)

    try:
        message = input('Enter message: ')
        messagen = message.encode()
        print('Sending: ' + message)
        client_socket.sendall(messagen)

        data = client_socket.recv(1024)
        datad = data.decode()
        print('Received: ' + datad)

    finally:
        print('Closing connection')
        client_socket.close()
if __name__ == '__main__':
    start_client()
