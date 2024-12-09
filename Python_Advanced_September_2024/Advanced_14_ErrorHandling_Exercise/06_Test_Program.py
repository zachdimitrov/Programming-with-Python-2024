import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(0.5)
for i in range(2, 256):
    ip = f"192.168.1.{i}"
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(0.5)
        client_socket.connect((ip, 8080))
        print(f"Server found: {ip}")
        break
    except TimeoutError:
        print(f"No connection to server {ip}!")
    time.sleep(1)


