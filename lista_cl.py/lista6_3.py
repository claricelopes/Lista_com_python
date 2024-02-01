n = int(input("digit o numero de pessoas participando: "))
soma = 0

for i in range(n):
    idade = int(input("digite sua idade: "))
    soma += idade 

media = soma/n

if 0 < media < 25:
    print("jovem")
elif 26 < media < 60:
    print("adulta")
else:
    print("idosa") 