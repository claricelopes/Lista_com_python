def pares(lista):
    lista_nova = []

    for i in range(10):
        if (lista[i] % 2 == 0):
            lista_nova.append(lista[i])
    print(lista_nova) 

numeros = []
for i in range (10):
    numeros.append(int(input('digite: ')))

pares(numeros) 
