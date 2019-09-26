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
#from bs4 import BeautifulSoup
#import re
import csv

url="https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv"

import csv
with open('https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv') as csvfile:
    csv_content = csv.reader(csvfile, delimiter=',')
    for row in csv_content:
      if row[2] == '2007':
          print(row[2], row[10])