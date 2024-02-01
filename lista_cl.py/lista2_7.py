valor_produto = float(input("digite o valor do produto comprado: "))
forma_pg = input("digite a forma de pagamento que deseja: ")

desconto = (valor_produto * 0.1) 

if valor_produto >= 100 and forma_pg == 'dinheiro':
    print(f"o valor final da compra é: {valor_produto - desconto}") 
else:
    print(f"o valor final da compra é: {valor_produto}") 