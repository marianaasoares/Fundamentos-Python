from threading import Thread

lista = [1.3, 10.4, 40.0, 59.87, 33.01, 101,4]*100
tamanho = len(lista)
nova_lista = []

def calcPorcent(lista):
    for i, valor in enumerate(lista):
        nova_lista.append(valor * 0.1)

t0 = Thread(target=calcPorcent, args=(lista[:tamanho//2],))
t0.start()

t1 = Thread(target=calcPorcent, args=(lista[:tamanho//2],))
t1.start()

t0.join()
t1.join()

print(nova_lista)