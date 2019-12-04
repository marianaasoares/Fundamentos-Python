import multiprocessing, time, random
from threading import Thread
[10000000, 20000000, 30000000]

def somaPorcent(q1, q2):
    listaporcent = q1.get()
    for i in range(len(listaporcent)):
        listaporcent[i] = listaporcent[i]*0.1
    q2.put(listaporcent)
    
def calcPorcent(lista, inicio, fim):
    for i, valor in enumerate(lista):
        lista[i] = lista[i] * 0.1
    
if __name__ == "__main__":
    
    for vez in [100, 150, 152]:
        lista = [1.3, 10.4, 40.0, 59.87, 33.01, 101.4]*vez
        tamanho = len(lista)
        n = 4
    
    # Captura tempo inicial
    t_inicio = float(time.time())
    
    NProc = 4 # Número de processos a ser criado
    # Fila de entrada dos processos
    q_entrada = multiprocessing.Queue()
    # Fila de saída dos processos
    q_saida = multiprocessing.Queue()
    lista_proc = []
    
    for i in range(NProc):
        ini = i * int(N/NProc) # início do intervalo da lista
        fim = (i + 1) * int(N/NProc) # fim do intervalo da lista
        q_entrada.put(lista[ini:fim])
        p = multiprocessing.Process(target=somaPorcent, args=(q_entrada,
        q_saida))
        p.start() # inicia processo
        lista_proc.append(p) # guarda o processo
        
    for p in lista_proc:
        p.join() # Espera os processos terminarem
    soma = []
    
    for i in range(0, NProc):
        soma.extend(q_saida.get())
        
    # Captura tempo final
    t_fim = float(time.time())
    
    #tempo sequencial
    lista = [1.3, 10.4, 40.0, 59.87, 33.01, 101.4]*1000
    t_seq_inicio = float(time.time())
    somaPorcent(0, N)
    t_seq_fim = float(time.time())
    
    # Imprime o resultado e o tempo de execução
    print("Soma:", soma)
    print("Tempo total:", t_fim - t_inicio)
    print(f"Tempo total {N}: {n : <10} {round(t_fim - t_inicio,3): 10} | SEQUENCIAL {round(t_seq_fim - t_seq_inicio):10}  ")

