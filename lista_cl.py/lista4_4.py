num1 = int(input("digite um numero: "))
num2 = int(input("digite um numero: "))
contador = 0

while (num1 >= num2): 
    num1 -= num2 
    contador += 1 


print(f"o resultado da divisão é: {contador}, com resto igual a {num1}")  