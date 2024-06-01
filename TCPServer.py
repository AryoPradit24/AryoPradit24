import socket
import threading
import os

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Received request:\n{request}")

    # Parse HTTP request
    headers = request.split('\n')
    filename = headers[0].split()[1]

    if filename == '/':
        filename = '/TugasBesarJarkom.html'

    try:
        # Open and read the requested file
        with open(filename[1:], 'rb') as file:
            response_data = file.read()

        # Send HTTP response header
        response_header = 'HTTP/1.1 200 OK\n'
        response_header += 'Content-Type: text/html\n'
        response_header += f'Content-Length: {len(response_data)}\n'
        response_header += '\n'

    except FileNotFoundError:
        # File not found, send 404 response
        response_header = 'HTTP/1.1 404 Not Found\n'
        response_header += 'Content-Type: text/html\n'
        response_header += '\n'
        response_data = b"<html><body><h1>404 Not Found</h1></body></html>"

    response = response_header.encode('utf-8') + response_data

    # Send response to client
    client_socket.sendall(response)
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 6789))
    server.listen(5)
    print("Server listening on port 6789...")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
