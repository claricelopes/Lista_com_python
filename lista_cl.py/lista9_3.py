def pares(list):
    numeros = [] 
    for i in list: 
        if i % 2 == 0:
            numeros.append(i) 
    print(numeros) 
   
num = []
for i in range(10):
    num.append(int(input("digite um numeros: ")))

pares(num)
    