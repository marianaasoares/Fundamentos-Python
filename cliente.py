import socket
from time import sleep

socket_family = socket.AF_INET
socket_type = socket.SOCK_STREAM

s = socket.socket (socket_family, socket_type)

try:
    # Tenta se conectar ao servidor
    s.connect(('172.18.0.98', 5200))
    msg = "Ola Mariana"
    s.send(msg.encode('ascii'))
    s.close()
except Exception as erro:
    print(str(erro))