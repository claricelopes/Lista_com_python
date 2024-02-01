codigo = int(input("digite o codigo do produto: "))
quant = int(input("digite a quantidade comprada: "))
valor1 = valor2 = valor3 = valor4 = valor5 = 0

while codigo != 0:
    if codigo == 1:
        valor1 = quant * 5.5 
    elif codigo == 2:
        valor2 = quant * 2.3
    elif codigo == 3:
        valor3 = quant * 4.75
    elif codigo == 4: 
        valor4 = quant * 6.8
    elif codigo == 5:
        valor5 = quant * 9.3
    else:
        print("código inválido") 
    codigo = int(input("digite o codigo do produto: "))
    quant = int(input("digite a quantidade comprada: "))
    
total = valor1 + valor2 + valor3 + valor4 + valor5 

print(f"o total da compra deu {total} R$")
