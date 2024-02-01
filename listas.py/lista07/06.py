pontos = [(2,4), (3,5), (8,13), (2,24), (17,21), (9,29)]   

lista = []
for i in pontos:
    menor_dist = 9999999999
    maior_dist = 0
    media_dist = 0
    for j in pontos:
        if i != j:
            dist = ((j[0] - i[0])**2 + (j[1] - i[1])**2)**(1/2) 
            if dist < menor_dist:
                menor_dist = dist 
            if dist > maior_dist:
                maior_dist = dist 
            media_dist += dist 
    lista.append([menor_dist, maior_dist, media_dist/len(pontos)]) 

for i in range(len(pontos)):
    print(f"ponto: {pontos[i]}:\n distância mínima: {lista[i][0]} distância máxima: {lista[i][1]}\n mádia de distância: {lista[i][2]}") 