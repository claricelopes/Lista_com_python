num = int(input("digite um numero: ")) 
contador = 0
soma = 0

while num >= 0:
    soma += num
    contador += 1
    num = int(input("digite um numero: "))  

media = soma/contador 
print(media)   