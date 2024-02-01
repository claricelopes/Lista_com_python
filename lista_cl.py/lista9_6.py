base = int(input("digite a base: "))
expoente = int(input("digite o expoente: "))
resultado = 1

for i in range(expoente):
    resultado *= base

print(resultado) 