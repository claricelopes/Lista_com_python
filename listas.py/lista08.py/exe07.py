num = (input("digite um número: "))

ex1 = {"1":"um", "2":"dois", "3":"três", "4":"quatro", "5":"cinco", "6":"seis", "7":"sete", "8":"oito", "9":"nove"}
ex10 = {"10": "dez", "11": "onze", "12":"doze", "13":"treze", "14":"quatorze", "15": "quinze", "16": "dezesseis", "17": "dezesete", "18": "dezoito", "19": "dezenove"}
ex20 = {"20":"vinte", "30": "trinta", "40": "quarenta", "50": "cinquenta", "60":"secenta", "70":"setenta", "80":"oitenta", "90": "noventa"} 

if len(num) == 1:
    print(ex1[num]) 
elif len(num) == 2:
    if int(num) < 20: 
        print(ex10[num]) 
    else: 
        print(f"{ex20[num[0]+'0']}  e  {ex1[num[1]]}") 