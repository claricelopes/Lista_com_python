'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
número elevado ao segundo número. Não utilize a função de potência da linguagem. 
'''
base = int(input("digite um número: "))
expoente = int(input("digite outro número: "))
resultado = 1

for i in range(1, expoente+1):
    resultado *= base
    
print(resultado)