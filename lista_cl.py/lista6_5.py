cand1 = 0
cand2 = 0
cand3 = 0

eleitores = int(input("digite o numero de eleitores: "))

for i in range(eleitores):
    voto = int(input("digite o numero do seu candidato: ")) 
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    else:
        print("numero invalido") 

print(f"numero de votos do candidato 1: {cand1}") 
print(f"numero de votos do candidato 2: {cand2}") 
print(f"numero de votos do candidato 3: {cand3}") 