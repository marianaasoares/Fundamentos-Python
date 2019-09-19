"""Usando o Thonny, escreva um programa em Python que some todos os números pares de 1 até um dado n, inclusive.
O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma."""


n = int(input("Digte um número: "))

soma = 0

for i in range(1,n):
    if i % 2 == 0:
        soma = soma + i
print(soma)    
        
    