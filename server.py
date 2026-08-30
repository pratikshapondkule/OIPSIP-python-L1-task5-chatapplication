import socket
import threading
from datetime import datetime

HOST = "localhost"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server started.")
print("Waiting for a client to connect...")

conn, address = server.accept()

print(f"Client connected: {address}")


def receive_messages():
    while True:
        try:
            message = conn.recv(1024).decode()

            if not message:
                print("Client disconnected.")
                break

            time = datetime.now().strftime("%H:%M")
            print(f"[{time}] Client: {message}")

        except:
            print("Connection closed.")
            break


thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()


while True:
    message = input()

    if message.lower() == "exit":
        break

    time = datetime.now().strftime("%H:%M")
    full_message = f"[{time}] Server: {message}"

    conn.send(full_message.encode())

conn.close()
server.close()