numero = (input("digite: "))

unidades = {"1": "um", "2":"dois", "3": "tres", "4": "quatro", "5": "cinco", "6": "seis", "7": "sete", "8": "oito", "9": "nove"} 
dezena = {"10": "dez",  "11": "onze", "12": "doze", "13": "treze", "14": "quatorze", "15": "quinze", "16": "dezesseis", "17": "dezesete", "18": "dezoito", "19": "desenove"}
dezena2 = {"20": "vinte", "30": "trinta", "40": "quarenta", "50": "cinquenta", "60": "sessenta", "70": "setenta", "80": "oitenta", "90": "noventa"}

if len(numero) == 1:
    print(unidades[numero])
elif len(numero) == 2:
    if int(numero) < 20:
        print(dezena[numero]) 
    else: 
        print(f"{dezena2[numero[0] + '0']} e {unidades[numero[1]]}")  