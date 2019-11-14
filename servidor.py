
import socket

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtém o nome da máquina
host = socket.gethostname()
porta = 5400
# Associa a porta
socket_servidor.bind((host, porta))
# Escutando...
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)

while True:
    # Aceita alguma conexão
    (socket_cliente,addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
    msg = socket_cliente.recv(1024)
    # Decodifica mensagem em ASCII
    print (msg.decode('ascii'))
    socket_cliente.close()

