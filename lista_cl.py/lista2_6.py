nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if 9.0 < media <= 10.0:
    print("A") 
elif 7.5 < media <= 9.0:
    print("B")
elif 6.0 < media <= 7.5:
    print("C")
elif 4.0 < media <= 6.0:
    print("D")
elif 0.0 < media <= 4.0: 
    print("E")  
else:
    print("invalido")  