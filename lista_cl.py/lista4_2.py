num = int(input("digite um numero: "))
maior_valor = 0
menor_valor = 999999
soma = 0 

while (num != -1):
    if num > maior_valor:
        maior_valor = num 
    if num < menor_valor:
        menor_valor = num 
    soma += num 
    num = int(input("digite um numero: ")) 

print(f"o maior valor foi: {maior_valor}")
print(f"o menor valor foi: {menor_valor}")
print(f"a soma é: {soma}") 
