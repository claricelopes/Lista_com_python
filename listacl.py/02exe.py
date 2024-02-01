deposito = float(input("digite o valor do deposito inicial: "))
taxa_juros = float(input("digite o valor da taxa de juros: "))
deposito_inicial = deposito 
meses = 0 

for i in range(1,25):
    deposito += (deposito * taxa_juros / 100) 
    meses += 1
    print(f"{meses}° mes: {deposito:.2f} R$") 

juros = (deposito - deposito_inicial)
print(f"o total recebido em juros foi : {juros:.2f} R$") 
