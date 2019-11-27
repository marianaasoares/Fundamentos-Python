import threading

Nthreads = 4
lista_thread =[]

def funcThread(i):
    print("Olá, eu sou a Thread:", i)

for i in range(Nthreads):
    t = threading.Thread(target=funcThread, args=(i,))
    t.start()
    lista_thread.append(t)

for t in lista_thread:
    t.join()