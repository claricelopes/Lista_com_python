num = int(input("digite um numero: "))

while num != -1: 
    if num % 2 == 0:
        print(f"{num*2}") 
    else:
        print(f"{num*3}") 
    num = int(input("digite um numero: ")) 