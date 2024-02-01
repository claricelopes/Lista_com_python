frase = input("digite: ") 

while frase != "-1":
    dicionario = {} 
    for i in frase: 
        contador = 0
        for j in frase:
            if i == j:
                contador += 1
            dicionario[i] = contador 
    print(dicionario)
    frase = input("digite: ") 