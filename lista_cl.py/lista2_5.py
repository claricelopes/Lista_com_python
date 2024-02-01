lado1 = int(input("digite um lado do triangulo: "))
lado2 = int(input("digite um lado do triangulo: "))
lado3 = int(input("digite um lado do triangulo: ")) 

if (lado1 == lado2 == lado3):
    print("esse é um triangulo equilátero")
elif (lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1):
    print("esse é um triangulo isosceles")
elif (lado1 != lado2 != lado3):
    print("esse é um triangulo escaleno")
else:
    print("esse triangulo não existe")  


