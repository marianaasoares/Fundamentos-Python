import os

def busca_arquivo(nome_diretorio, nome_arquivo):
    lista_arquivos = []
    if os.path.isdir(nome_diretorio):
        lista_arquivos = os.listdir(nome_diretorio)
    for elemento in lista_arquivos:
        print(elemento)
        if os.path.isfile(os.path.join(diretorio, elemento)) == True:
            if nome_arquivo in lista_arquivos:
                return True
        else:
            try:
                if busca_arquivo(os.path.join(diretorio, elemento), nome_arquivo):
                    return True
            except PermissionError:
                pass
    return False

nome_arquivo = input("Digite o nome do arquivo que quer encontrar: ")
nome_diretorio = input("Digite o diretório que deseja procurar o arquivo: ")

busca_arquivo(nome_diretorio, nome_arquivo)