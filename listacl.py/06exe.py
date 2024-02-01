n = int(input("digite um número: "))
num = 1 
anterior1 = 1
anterior2 = 1 

for i in range(1, n+1):
    if i < 3:
        print(1)
    else:
        num = anterior1 + anterior2  
        print(num)
        anterior1 = anterior2 
        anterior2 = num 