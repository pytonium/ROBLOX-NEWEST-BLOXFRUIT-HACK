import socket
import threading
HOST = '' 
def handle_client(client_socket, addr):
    print(f"[+] Connection from {addr}")
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8', errors='ignore')
            if not data:
                break
            print(f"[{addr}] {data}", end='', flush=True)
    except:
        pass
    finally:
        client_socket.close()
        print(f"{addr} disconnected")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, 4444))
server.listen(5)
while True:
    client_sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_sock, addr))
    client_thread.daemon = True
    client_thread.start()