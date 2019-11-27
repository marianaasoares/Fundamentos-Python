from threading import Thread
import time

lista = [1.3, 10.4, 40.0, 59.87, 33.01, 101,4]*100
tamanho = len(lista)

t_inicio = float(time.time())

#for vez in [100000, 100000, 100000,]:
    #lista = [1.3, 10.4, 40.0, 59.87, 33.01, 101,4]*vez
    

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

t_fim = float(time.time())

#Tempo sequencial 
lista = [1.3, 10.4, 40.0, 59.87, 33.01, 101,4]*10000
t_seq_inicio = float(time.time())
calcPorcent(lista, 0, tamanho)
t_fim_seq = float(time.time())
print(f"Tempo total: seq = {round(t_fim_seq - t_seq_inicio, 5)}")

print("Esta linha é impresa após a execução das duas threads")
print(lista)

print("Tempo total Sequencial em segundos:", t_fim - t_inicio)

print(f"Tempo total para uma lista de tamanho {tamanho}: {n} Threads = {round(t_fim - t_inicio, 5)} | seq = {round(t_fim_seq - t_seq_inicio, 5)}")