import os

def busca_arquivo(nome, dir):
    l = []
    try:
        l = os.listdir(dir)
    except:
        pass
    for i in l:
        if os.path.isfile(i) and i == nome:
            return(True)
    return(False)

nome_arq = input("Entre com o nome do arquivo: ")
nome_dir = input("Entre com o nome do diretório: ")

if busca_arquivo(nome_arq, nome_dir):
    print(nome_arq, "Não foi encontrado", nome_dir)
else:
    print(nome_arq, "não foi encontrado em", nome_dir)