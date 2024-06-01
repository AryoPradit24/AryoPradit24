import socket
import threading

# Konfigurasi server
HOST = '127.0.0.1'  # Localhost
PORT = 6789         # Port server

def handle_client_connection(client_socket):
    request = client_socket.recv(1024).decode()
    print(f"Received request: {request}")
    
    # Parsing permintaan HTTP
    headers = request.split('\n')
    filename = headers[0].split()[1]
    
    # Jika file yang diminta adalah root, arahkan ke HelloWorld.html
    if filename == '/':
        filename = '/HelloWorld.html'
    
    try:
        # Buka file yang diminta
        with open(filename[1:], 'r') as f:
            content = f.read()
        
        # Membuat HTTP response
        response = 'HTTP/1.1 200 OK\n'
        response += 'Content-Type: text/html\n'
        response += 'Content-Length: {}\n'.format(len(content))
        response += '\n'
        response += content
    except FileNotFoundError:
        # Jika file tidak ditemukan, kirim 404 Not Found
        response = 'HTTP/1.1 404 Not Found\n'
        response += 'Content-Type: text/html\n'
        response += '\n'
        response += '<html><body><h1>404 Not Found</h1></body></html>'
    
    # Mengirimkan respon ke klien
    client_socket.sendall(response.encode())
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server started at {HOST}:{PORT}")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        handle_client_connection(client_socket)

if __name__ == "__main__":
    start_server()
