import socket

def send_message(message, host='127.0.0.1', port=5000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        client_socket.send(message.encode())

        reply = client_socket.recv(1024).decode()
        print(f"[Soulwave Server Replay] {reply}")
    except Exception as e:
        print(f"[Error] {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    send_message("Hello from Gepeta!")
