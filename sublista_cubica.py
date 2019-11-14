sublista = [-15, 7, -6, 2, 1, 10]

lista_de_somas = []

for index, elemento in enumerate(sublista):
    for index2, elemento2 in enumerate(sublista):
        if index2 >= index:
            lista_de_somas.append(sum(sublista[index:index2+1]))
print(max(lista_de_somas))
    
    