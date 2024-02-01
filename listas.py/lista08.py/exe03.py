CPF = input("digite seu CPF: ") 

if CPF[3] == "." and CPF[7] == "." and CPF[11] == "-": 
    print("CPF válido")
else: 
    print("CPF inválido") 