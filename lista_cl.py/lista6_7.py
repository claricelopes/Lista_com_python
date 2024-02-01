num = int(input("digite um numero: "))
cont1 = 0 

for i in range(num, 2, -1): 
    resto = num % i
    if resto == 0: 
        cont1 += 1 
    else: 
        cont1 == 0 

print(cont1) 

if cont1 <= 1 or num == 1 or num == 2: 
    print("é primo")
else:
    print("é nao primo") 