num = int(input("digite um número: "))
contp = 0 

for i in range(num, 0,-1):
    if num % i == 0:
        contp += 1
    else: 
        contp == 0 


print(contp)
if contp == 2 or num == 1 or num==2:
    print("o número digitado e primo") 
else: 
    print("o número digitado nao é primo") 
