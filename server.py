import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 65432)
    print('Starting server on {} port {}'.format(*server_address))
    server_socket.bind(server_address)

    server_socket.listen(1)

    end = False

    while True:
        print('Waiting for a connection...')
        connection, client_address = server_socket.accept()
        try:
            print('Connection from', client_address)

            while True:
                data = connection.recv(1024)
                if data:
                    decoded_data = data.decode()
                    print('Received:', decoded_data)

                    if decoded_data == 'end':
                        end = True
                        break

                    encoded_data = decoded_data.encode()
                    print('Sending data back to the client')
                    connection.sendall(encoded_data)
                else:
                    print('No data from', client_address)
                    break
            if end:
                connection.close()
                break
        finally:
            connection.close()

if __name__ == '__main__':
    start_server()
