n = int(input("digite o número de pessoas participantes: "))
soma = 0 

for i in range(n):
    idade = int(input("digite sua idade: "))
    soma += idade 

media = (soma / n) 

if(0 < media <= 25):
    print("turma jovem")
elif(26 <= media <= 60):
    print("turma adulta") 
elif(media > 60):
    print("turma idosa")
else:
    print("média inválida") 

