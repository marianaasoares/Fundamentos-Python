"""Escreva uma função em Python que leia uma tupla contendo números inteiros, retorne uma lista contendo somente os números ímpares e uma nova tupla
contendo somente os elementos nas posições pares."""

primeira_tupla = (10, 3, 6, 2, 23)

def lista_impares(primeira_tupla):
    impares = []
    for i in primeira_tupla:
        if i % 2 == 1:
            impares.append(i)
    return (impares)

def tupla_pares(primeira_tupla):
    pares = []
    n = 0
    for i in primeira_tupla:
        if n % 2 == 0:
            pares.append(i)
        n = n + 1
    return tuple(pares)   
        
            
print(lista_impares(primeira_tupla))
print(tupla_pares(primeira_tupla))

