import socket

def start_server(host='0.0.0.0', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"[Soulwave Server] Listening on {host}:{port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[Soulwave Server] Conection from {addr}")

        data = client_socket.recv(1024).decode()
        print(f"[Message Received] {data}")

        reply = "Messaging received loud and clear!"
        client_socket.send(reply.encode())

        client_socket.close()

if __name__ == "__main__":
    start_server()
