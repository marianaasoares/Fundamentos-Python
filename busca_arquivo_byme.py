import os

def procura_arquivo(nome_diretorio, nome_arquivo):
    lista_arquivos = []
    lista_arquivos.extend(os.listdir(nome_diretorio))
    for elemento in lista_arquivos:
        if os.path.isfile(elemento):
            if elemento == nome_arquivo:
                print(elemento, "É um Arquivo e ACHEI")       
        else:
            print(elemento, "Não é um arquivo")
            
            
            
nome_arquivo = input("Digite o nome do arquivo que quer encontrar: ")
nome_diretorio = input("Digite o diretório que deseja procurar o arquivo: ")

procura_arquivo(nome_diretorio, nome_arquivo)