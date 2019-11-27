from random import randint
lista1 = []
lista2 = []
lista3 = []

for i in range(10):
    lista1.append(randint(0, 10))
    lista2.append(randint(0, 10))
    
for item1, item2 in zip(lista1, lista2):
    soma = item1 + item2
    lista3.append(soma)

print(lista3)
