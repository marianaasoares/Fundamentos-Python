"""Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv
E:
Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega, verifique: No século XXI (a partir de 2001), qual foi o maior medalhista de ouro, considerando apenas as seguintes modalidades:
Curling
Patinação no gelo (skating)
Esqui (skiing)
Hóquei sobre o gelo (ice hockey)
Para cada esporte, considere todas as modalidades, tanto no masculino quanto no feminino. Sua resposta deve imprimir um relatório mostrando o total de medalhas de cada um dos países e em que esporte, ano, cidade e gênero (masculino ou feminino) cada medalha foi obtida."""

import requests
import csv
url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv"
r = requests.get(url)
text = r.text
reader = csv.reader(r.iter_lines(decode_unicode=True), delimiter=',')

#incrementador
i=0
# Países Nórdicos solicitados
suecia=0
dinamarca=0
noruega=0

#Array com os esportes solicitados
Esportes = ["Curling", "Skiing","Skating","Ice Hockey"]

for linha in reader:
    if i > 0:
        if int(linha [0]) > 2000: #Pega linha com os anos se for do século XXI 
            if linha[4] == "SWE" and linha[7] == "Gold" and linha [2] in Esportes: #Pega o nome do pais + se tem medalha de ouro + o esporte corresponte a array criado
                suecia=suecia+1 #armazena as informações na variável do país
                print(linha)   #printa a linha
            if linha[4] == "DEN" and linha[7] == "Gold" and linha [2] in Esportes: #Pega o nome do pais + se tem medalha de ouro + o esporte corresponte a array criado
                dinamarca=dinamarca+1  #armazena as informações na variável do país
                print(linha) #printa a linha
            if linha[4] == "NOR" and linha[7] == "Gold" and linha [2] in Esportes: #Pega o nome do pais + se tem medalha de ouro + o esporte corresponte a array criado
                noruega=noruega+1 #armazena as informações na variável do país
                print(linha)  #printa a linha     
    i = i+1 
