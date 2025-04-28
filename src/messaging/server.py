import socket
from src.encryption.encryptor import encrypt_message, decrypt_message
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY').encode()

def start_server(host='0.0.0.0', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"[Soulwave Server] Listening on {host}:{port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[Soulwave Server] Connection from {addr}")


        while True:
            try:
                encrypted_data = client_socket.recv(4096)
                if not encrypted_data:
                    print ("[Client disconnected]")
                    break
                data = decrypt_message(encrypted_data, SECRET_KEY)
                print(f"You: {data}")

                reply = encrypt_message("Message received!", SECRET_KEY)
                client_socket.send(reply)

            except ConnectionResetError:
                print("[Connection was forcibly closed by client]")
                break

        client_socket.close()

if __name__ == "__main__":
    start_server()
