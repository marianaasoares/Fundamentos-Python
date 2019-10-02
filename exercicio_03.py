"""Usando o Thonny, escreva uma função em Python chamada potencia.
Esta função deve obter como argumentos dois números inteiros, A e B, e calcular AB usando multiplicações sucessivas
(não use a função de python math.pow) e retornar o resultado da operação.
Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função."""

base = int(input("Digite o valor da base: "))
potencia = int(input("Digite o valor da potencia: "))

resultado = 1
incrementador = 0
while incrementador < potencia:
    resultado = resultado * base
    incrementador = incrementador + 1 

print("O valor da potenciação é: ", resultado)