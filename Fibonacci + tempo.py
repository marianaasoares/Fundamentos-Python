import os
time_result_inicial = os.times()

primeiro_fibonacci = 0
segundo_fibonacci = 1
for i in range(2, 35):
    fibonacci_proximo = segundo_fibonacci + primeiro_fibonacci
    print(f"F({i}) = {fibonacci_proximo}")
    primeiro_fibonacci = segundo_fibonacci
    segundo_fibonacci = fibonacci_proximo
        
time_result_final = os.times()
print(time_result_final.user - time_result_inicial.user)
        