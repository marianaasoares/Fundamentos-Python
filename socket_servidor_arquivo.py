import socket
import os

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nome_maquina = socket.gethostname()
porta = 6000

socket_servidor.bind((nome_maquina, porta))

socket_servidor.listen()
print("Servidor de nome", nome_maquina, "esperando conexão com a porta", porta)

while True:
    (socket_cliente, addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
    mensagem = socket_cliente.recv(2048)
    nome_arquivo = mensagem.decode('ascii')
    if os.path.isfile(nome_arquivo):
        tamanho = os.stat(nome_arquivo).st_size
        socket_cliente.send(str(tamanho).encode('ascii'))
        arquivo = open(nome_arquivo, 'rb')
        bytes = arquivo.read(4096)
        while bytes:
            socket_cliente.send(bytes)
            bytes = arquivo.read(4096)
        arquivo.close()
    else:
        print("Não encontrou o arquivo")
        socket_cliente.send('-1'.encode('ascii'))
    socket_cliente.close()
    
socket_servidor.close()