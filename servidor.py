import socket


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind(("127.0.0.1" , 9000))
servidor.listen(1)
print("Servidor esperando conexão na porta 9000)")

conn,addr = servidor.accept()
print(f"Conexão estabelecida com {addr}")

while True:
    try:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Recebi: {data.decode()}")
        conn.sendall(data.upper())
    except (ConnectionResetError, ConnectionAbortedError, OSError):
        print("Conexão perdida com o cliente.")
        break

conn.close()
servidor.close()