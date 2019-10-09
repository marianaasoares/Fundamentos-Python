import os

print("O sistema operacional é: ", os.name) #printa o nome do sistema operacional
print("Usuário atual: ", os.getlogin()) # printa o nome do usuário
print("Variáveis do sistema: ", os.environ) # printa as variávis do sistema
print(os.environ['HOMEDRIVE']) #Printa variáveis específicas
print(os.environ['HOMEPATH']) #Printa variáveis específicas
print(os.getcwd()) #Printa o caminho completo do diretório corrente
print(os.getpid()) #Printa o PID do próprio processo em execução, imprime o valor

