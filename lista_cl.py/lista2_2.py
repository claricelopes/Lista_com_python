genero = input("digite seu genero (F/M): ")
altura = float(input("digite sua altura: "))

peso_feminino = (62.1*altura) - 44.7
peso_masculino = (72.7*altura) - 58

if genero == 'F':
    print(f"seu peso ideal é: {peso_feminino:.2f}") 
elif genero == 'M':
    print(f"seu peso ideal é: {peso_masculino:.2f}")  
else:
    print("letra inválida") 