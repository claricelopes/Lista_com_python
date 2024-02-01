lista_altura = []

lista_sexo = []

for x in range (10):
    altura = float ( input ( "digite a altura: "))

    sex = input("digite o sexo (M/F): ")

    lista_altura.append(altura)

    lista_sexo.append(sex)

menor = maior = altura

contadorM = contadorF = 0

media_homem = 0

media_mulher = 0

sex_menor = sex_maior = sex

for x in range (10):

    if (lista_altura[x] >= maior):
        maior = float(lista_altura[x])
        sex_maior = lista_sexo[x]
    
    elif (lista_altura[x] <= menor):
        menor = float(lista_altura[x])
        sex_menor = lista_sexo [x]
    

for i in range (10):

    if "M" == lista_sexo[i] or "m" == lista_sexo[i]:
        media_homem += float(lista_altura[i])
        contadorM += 1
    else:
        media_mulher += float(lista_altura[i])
        contadorF += 1

print (f"maior foi {maior:.2f} metros do sexo {sex_maior} \n e a menor foi de {menor:.2f} metros do sexo {sex_menor}. ")

print(f"a média de altura dos homens foi de {(media_homem/contadorM):.2f} e a média das mulheres foi de {(media_mulher/contadorF):.2f}.")

print (f"foram {contadorM} homens e {contadorF} mulheres.") 