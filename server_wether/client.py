import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 1010

client_socket.connect((host, port))

server_message = client_socket.recv(1024).decode()
print(server_message)

while True:
    client_message = input('Enter the city for weather forecast: ')

    if not client_message:
        print('Disconnecting from the server...')
        break

    client_socket.send(client_message.encode())

    server_response = client_socket.recv(2048).decode()
    print(f'Server response:\n{server_response}')

client_socket.close()

