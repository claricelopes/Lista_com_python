def contagem(str):
    dicionario = {} 
    for i in str:
        contador = 0
        for j in str:
            if i == j:
                contador += 1
            dicionario[i] = contador 
    print(dicionario) 


frase = input("digite: ")

contagem(frase) 