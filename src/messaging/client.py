import socket

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

        client_socket.send(message.encode())

        reply = client_socket.recv(1024).decode()
        print(f"Soulwave: {reply}")

    except Exception as e:
        print(f"[Error] {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    send_message()
