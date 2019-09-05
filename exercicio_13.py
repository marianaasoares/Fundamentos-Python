"""Obtenha, usando requests ou urllib, o conteúdo sobre as PyLadies no link http://brasil.pyladies.com/about e:
Conte todas as palavras no corpo da página, e indique quais palavras apareceram apenas uma vez.
Conte quantas vezes apareceu a palavra ladies no conteúdo da página"""

import requests
from bs4 import BeautifulSoup
import re
from collections import defaultdict

url = "http://brasil.pyladies.com/about/"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
palavras = []
contador_palavras = defaultdict(int)
for i in soup.html.body.find_all('p'):
    text = re.sub(' +',' ',i.text)
    text = re.sub('\n','',text)
    if text is not " ":
        for palavra in text.split(" "):
            contador_palavras[palavra.lower()] += 1
            
contador = []
for item in contador_palavras.items():
    if item[1] == 1:
        contador.append((item[0], item[1]))
contador.sort(key=lambda x : x[1])
print(contador)

print("Ladies aparece ",contador_palavras["ladies"], " vezes no texto.")

