import random 

lista = [] 
cont_1 = 0
cont_2 = 0
cont_3 = 0
cont_4 = 0
cont_5 = 0
cont_6 = 0

n = int(input('digite o numero de lançamentos: ')) 
percentual = (100/n) 

while n > 0:    
    for i in range(n): 
        numero = (random.randint(1,6))
        lista.append(numero)
    for i in lista:  
        if i == 1:
            cont_1 += percentual
        elif i == 2:
            cont_2 += percentual
        elif i == 3:
            cont_3 += percentual
        elif i == 4:
            cont_4 += percentual
        elif i == 5:
            cont_5 += percentual
        elif i == 6:
            cont_6 += percentual    
    print(f'o numero 1 teve {cont_1}%') 
    print(f'o numero 2 teve {cont_2}%') 
    print(f'o numero 3 teve {cont_3}%') 
    print(f'o numero 4 teve {cont_4}%') 
    print(f'o numero 5 teve {cont_5}%') 
    print(f'o numero 6 teve {cont_6}%') 
    n = int(input('digite o numero de lançamentos: ')) 

