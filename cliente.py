import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9000))

mensagem = input("Digite algo: ")
s.sendall(mensagem.encode())


resposta = s.recv(1024)
print(f"Resposta do servidor: {resposta.decode()}")

s.close()
