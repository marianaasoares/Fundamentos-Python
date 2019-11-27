import threading

def funcThread(i):
    print("Olá, eu sou a Thread:", i)
    
t0 = threading.Thread(target=funcThread, args=(0,))
t0.start()

t1 = threading.Thread(target=funcThread, args=(1,))
t1.start()

t0.join()
t1.join()