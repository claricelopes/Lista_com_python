import random as r

palavras = ["casa", "colher", "pente", "borboleta", "sapato"] 

palavra_esc = r.choice(palavras)
espaços = ["_" for i in range(len(palavra_esc))]
cont = [] 

total = 0

final = False 
for i in espaços:
    print(i, end=" ")
print("\n")
while final == False: 
    contador = -1
    letra = input("digite uma letra: ") 
    if letra in palavra_esc:
        cont.append(letra)
        for i in palavra_esc:
            contador += 1
            if letra == i:
                espaços[contador] = letra
        for i in espaços:
            print(i, end=" ")
        print("\n")
    else:
        total += 1
        print(f"você errou pela {total}° vez.\nTente novamente!") 
    
    if total == 6:
        print(f"você perdeu, a palavra é {palavra_esc}")

    digitada = ""
    for i in espaços:
        digitada += i
    if digitada == palavra_esc:
        print("você ganhou!") 
        final = True 