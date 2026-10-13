import socket

alvo = "127.0.0.1"

for porta in range (1, 1025):
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.settimeout(0.5)
    resultado = s.connect_ex((alvo, porta))
    if resultado == 0:
        print(f"Porta {porta} aberta")
        s.close()