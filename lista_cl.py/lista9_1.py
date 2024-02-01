cand10 = 0 
cand12 = 0 
votos = []

for i in range(10):
    votos.append(int(input("digite o numero do seu candidato: ")))
    if votos[i] == 10:
        cand10 += 1
    elif votos[i] == 12:
        cand12 += 1
    else: 
        print("numero invalido")

print(votos)
print(f"cand10: {cand10}")
print(f"cand12: {cand12}") 