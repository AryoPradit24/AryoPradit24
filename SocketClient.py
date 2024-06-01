import socket
import threading
import os

# Fungsi untuk menangani permintaan klien
def handle_client(client_socket, request):
    try:
        # Parsing permintaan HTTP
        filename = request.split()[1]
        if filename == "/":
            filename = "/TugasBesarJarkom.html"
        
        # Validasi ekstensi file
        if not filename.endswith(".html"):
            raise FileNotFoundError
        
        # Membuka file yang diminta
        with open("." + filename, "rb") as f:
            response_data = f.read()
            response_headers = "HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {}\n\n".format(len(response_data))
            client_socket.send(response_headers.encode() + response_data)
    except FileNotFoundError:
        # Jika file tidak ditemukan, kirim respons "404 Not Found"
        not_found_response = "HTTP/1.1 404 Not Found\n\n<html><body><h1>404 Not Found</h1></body></html>"
        client_socket.send(not_found_response.encode())
    finally:
        client_socket.close()

# Fungsi utama untuk menerima koneksi dan membuat thread baru
def start_server(server_host, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)
    print("Server listening on port {}...".format(server_port))
    
    while True:
        client_socket, _ = server_socket.accept()
        request = client_socket.recv(1024).decode()
        print("Received request: ", request)
        client_handler = threading.Thread(target=handle_client, args=(client_socket, request))
        client_handler.start()

if __name__ == "__main__":
    server_host = "127.0.0.1"  # Ganti dengan IP host Anda
    server_port = 8080  # Ganti dengan port yang Anda inginkan
    start_server(server_host, server_port)
