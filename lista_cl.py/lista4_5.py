divida_inicial = float(input("digite o valor inicial da divida:  "))
juro = float(input("digite o valor do juros mensal: "))
valor_mensal = float(input("digte o valor mensal que será pago: ")) 
divida = divida_inicial
contador = 0

while (divida > 0): 
    divida += (divida * (juro/100)) 
    divida_resto = divida - valor_mensal 
    contador += 1

total_pago = valor_mensal*contador 
total_juros = total_pago - divida_inicial

print(f"total de meses: {contador}") 
print(f"o total pago: {total_pago}") 
print(f"total de juros pago: {total_juros}")  
