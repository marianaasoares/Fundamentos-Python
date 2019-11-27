from threading import Thread

lista1 = [1.3, 10.4, 40.0, 59.87, 33.01, 101,4]*10000
tamanho1 = len(lista1)
lista2 = [3.5, 8, 14, 21.4, 89.3, 2.96, 100, 7]*10000
tamanho2 = len(lista2)
lista3 = []

def calcPorcent(lista, inicio, fim):
    for i, valor in enumerate(lista):
        lista[i] = lista[i] * 0.1

minhas_threads = []
n = 5
for i in range(n):
    inicio = i*(tamanho//n)
    fim = (i+1) * (tamanho//n)
    print(inicio, fim)
    t = Thread(target=calcPorcent, args=(lista, inicio, fim))
    minhas_threads.append(t)
    t.start()
    
for t in minhas_threads:
    t.join()

for item1, item2 in zip(lista1, lista2):
    soma = item1 + item2
    lista3.append(soma)
print(lista3)