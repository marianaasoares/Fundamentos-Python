"""Obtenha, usando requests ou urllib, a página HTML https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html dentro de seu programa em Python e faça:

    A) Imprima o conteúdo referente apenas à tabela apresentada na página indicada."""

import requests
from bs4 import BeautifulSoup

url = 'https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html'
csv = requests.get(url).text
html = csv
bs = BeautifulSoup(html, 'html.parser')


print(bs.body.div.article.center.div.text)

""" B) Escreva um programa que obtenha do usuário uma sigla do estado da região Centro-Oeste e apresenta suas informações correspondentes na tabela.
O resultado deve apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer. Não esqueça de checar se a sigla pertence à região."""


sigla = input("Digite a sigla correspondente a um estado do Centro-Oeste: ")

Estados_CO = ["MT", "MS", "GO", "DF"]

for i in bs.html.body.find('')




    