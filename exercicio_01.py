"""Usando o Thonny, escreva um programa em Python que leia uma tupla contendo 3 números inteiros,
(n1, n2, n3) e os imprima em ordem crescente."""

numeros = (10,9,8)

numeros_crescente = sorted(numeros, key=int)
print(numeros_crescente)
