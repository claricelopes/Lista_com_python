def ocorrencias(char, string):
    cont = 0
    for i in string:
        if i.lower() == char.lower():
            cont += 1
    return cont


palavra = input("digite uma palavra: ") 

contagem = {}

for i in palavra: 
    if i not in contagem:
        contagem[i] = ocorrencias(i, palavra)

print(contagem) 
