import socket
from src.encryption.encryptor import encrypt_message, decrypt_message
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY').encode()

def send_message(host='127.0.0.1', port=5000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print("[Connected to Soulwave Server]")

        while True:
            message = input ("You: ")
            if message.lower() == 'exit':
                print("[Disconnecting from server]")
                break

            encrypted = encrypt_message(message, SECRET_KEY)
            client_socket.send(encrypted)

            encrypted_reply = client_socket.recv(4096)
            reply = decrypt_message(encrypted_reply, SECRET_KEY)
            print(f"Soulwave: {reply}")

    except Exception as e:
        print(f"[Error] {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    send_message()
