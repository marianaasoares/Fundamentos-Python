import socket, sys, os

def imprime_status(bytes, tam):
    kbytes = bytes/1024
    tam_bytes = tam/1024
    texto = 'Baixando... '
    texto = texto + '{:<.2f}'.format(kbytes) + ' KB '
    texto = texto + 'de ' + '{:<.2f}'.format(tam_bytes) + ' KB'
    print(texto)

cria_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nome_arquivo = input("Entre com o nome do arquivo: ")

try:
    cria_socket.connect((socket.gethostname(), 6000))
    cria_socket.send(nome_arquivo.encode('ascii'))
    mensagem = cria_socket.recv(12)
    tamanho = int(mensagem.decode('ascii'))
    if tamanho >= 0:
        arquivo = open(f"./{nome_arquivo}", "wb")
        soma = 0
        bytes = cria_socket.recv(4096)
        while bytes:
            arquivo.write(bytes)
            soma = soma + len(bytes)
            os.system('cls')
            imprime_status(soma, tamanho)
            bytes = cria_socket.recv(4096)
        arquivo.close()
    else:
        print('Arquivo não encontrado no servidor!')
except Exception as erro:
    print(str(erro))

cria_socket.close()

input("Pressione qualquer tecla para sair...")