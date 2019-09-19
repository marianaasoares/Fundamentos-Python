"""Usando o Thonny, escreva uma função em Python chamada potencia.
Esta função deve obter como argumentos dois números inteiros, A e B, e calcular AB usando multiplicações sucessivas
(não use a função de python math.pow) e retornar o resultado da operação.
Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função."""


n1 = int(input("Digte o 1º número que será a base para fazer a potenciação: "))
n2 = int(input("Digte o 2º número que será o expoente para fazer a potenciação: "))


potenciacao = n1 ** n2
print(potenciacao)