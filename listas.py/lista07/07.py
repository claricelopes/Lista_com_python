palavra =  input ("digite a frase: ")  
lista = [] 

while (palavra != "-1"):
    dicionario = {}
    lista.append(palavra)
    for i in palavra:
        contador = 0
        for j in palavra:
            if i == j:
                contador += 1
        dicionario [i] = contador
    print (dicionario)
    
    palavra = input ("digite a frase: ")  