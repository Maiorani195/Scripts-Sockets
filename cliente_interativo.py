import socket
from datetime import datetime

Host = "127.0.0.1"
Porta = 9000

historico_de_sessoes = []
bytes_enviados = 0
bytes_recebidos = 0


def registrar(tipo, conteudo):
    hora = datetime.now().strftime("%H:%M:%S")
    historico_de_sessoes.append(f"[{hora}] {tipo}: {conteudo}")


def mostrar_historico():
    print("\nHistórico de Sessões:")
    for registro in historico_de_sessoes:
        print(registro)


def main():
    global bytes_enviados, bytes_recebidos

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    try:
        s.connect((Host, Porta))
        print(f"Conectado ao servidor {Host}:{Porta}")
    except ConnectionRefusedError:
        print(f"Não foi possível conectar ao servidor {Host}:{Porta}")
        return

    while True:
        mensagem = input("  >  ").strip()

        if mensagem.lower() == "sair":
            break

        if mensagem.lower() == "historico":
            mostrar_historico()
            continue

        if not mensagem:
            continue

        dados = mensagem.encode()
        s.sendall(dados)
        bytes_enviados += len(dados)
        registrar("Enviado", mensagem)

        try:
            resposta = s.recv(1024)
        except socket.timeout:
            print("Tempo limite ao receber resposta do servidor.")
            continue

        if not resposta:
            print("Conexão encerrada pelo servidor.")
            break

        texto_resposta = resposta.decode()
        bytes_recebidos += len(resposta)
        registrar("Recebido", texto_resposta)
        print(f"Resposta do servidor: {texto_resposta}")

    s.close()
    mostrar_historico()
    print("Sessão encerrada.")


if __name__ == "__main__":
    main()
