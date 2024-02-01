valor_produto = float(input("digite o valor do produto comprado: "))
forma_pg = input("digite a forma de pagamento que deseja: ")

desconto = (valor_produto * 0.1) 

if valor_produto >= 100 and forma_pg == 'dinheiro':
    print(f"o valor final da compra é: {valor_produto - desconto}") 
elif forma_pg == 'cheque':
    print(f"o valor final da compra é {valor_produto}") 
elif forma_pg == 'cartão':
    funcoes = input("digite a função de pagamento deb/cre: ")
    if funcoes == 'debito':
        print(f"o valor final da compra é: {valor_produto}")
    elif funcoes == 'credito':
        parcelas = int(input("digite o numero de parcelas que deseja: "))
        if parcelas == 1:
            print(f"{valor_produto}R$, 1 parcela de {valor_produto}")
        elif parcelas == 2:
            print(f"{valor_produto}, 2 parcelas de {valor_produto/2:.2f}") 
        elif parcelas == 3:
            print(f"{valor_produto}, 3 parcelas de {valor_produto/3:.2f}")  
        else:
            print("quantidade de parcelas invalida") 