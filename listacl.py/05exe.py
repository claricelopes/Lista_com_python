eleitores = int(input("digite o número total de eleitores: ")) 
print("candidato_1 = 10")
print("candidato_2 = 11")
print("candidato_3 = 12")  
cont1 = 0
cont2 = 0
cont3 = 0 

for i in range(eleitores): 
    voto = int(input("digite o numero do seu candidato: ")) 
    if voto == 10:
        cont1 += 1
    elif voto == 11:
        cont2 += 1
    elif voto == 12:
        cont3 += 1
    else:
        print("número inválido") 

print(f"o candidato_1 teve {cont1} votos")
print(f"o candidato_2 teve {cont2} votos")
print(f"o candidato_3 teve {cont3} votos") 