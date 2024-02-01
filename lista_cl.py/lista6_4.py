base = int(input("digite um numero: "))
expoente = int(input("digite um numero: "))
resultado = 1

for i in range(1, expoente+1):
    resultado *= base 

print(resultado) 