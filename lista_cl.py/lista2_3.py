ganho_pHora = float(input("digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("digite o numero de horas que você trabalha no mês: : "))

salario_total = (ganho_pHora * horas_trabalhadas)

Imposto_renda = (salario_total * 0.11)
inss = (salario_total * 0.08)
sindicato = (salario_total * 0.05)
descontos = (Imposto_renda + inss + sindicato) 

salario_liquido = salario_total - descontos

print(f"salario bruto: {salario_total}")
print(f"Imposto de renda: {Imposto_renda}")
print(f"INSS: {inss}")
print(f"sindicato: {sindicato}")
print(f"salario liquido: {salario_liquido}") 
