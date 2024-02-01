deposito_inicial = float(input("digite o valor do deposito inicial: "))
taxa_juros = float(input("digite a taxa de juros: "))
deposito = deposito_inicial

for i in range(25):
    deposito += (deposito * (taxa_juros/100))  
    print(f"valor para o {i} mes: {deposito:.2f} R$")  

ganho_juros = deposito - deposito_inicial 

print(f"o ganho com juros foi de: {ganho_juros:.2f} R$") 

