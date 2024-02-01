cont1 = cont2 = cont3 = cont4 = cont5 = cont6 = 0 

for i in range(20):
    voto = input("digite: ")
    if voto == "1":
        cont1 += 1
    elif voto == "2":
        cont2 += 1
    elif voto == "3":
        cont3 += 1
    elif voto == "4":
        cont4 += 1
    elif voto == "5":
        cont5 += 1
    elif voto == "6":
        cont6 += 1 
    else: 
        print("voto invalido")  

perc1 = (cont1/20*100) 
perc2 = (cont2/20*100) 
perc3 = (cont3/20*100) 
perc4 = (cont4/20*100)
perc5 = (cont5/20*100)
perc6 = (cont6/20*100) 

if cont1 > cont2 and cont1 > cont3 and cont1 > cont4 and cont1 > cont5 and cont1 > cont6:
    print(f"Java, vencedor! com {cont1} e {perc1}")   
elif cont2 > cont3 and cont2 > cont4 and cont2 > cont5 and cont2 > cont6 and cont2 > cont1:
    print(f"Python, vencedor! com {cont2} e {perc2}")
elif cont3 > cont4 and cont3 > cont5 and cont3 > cont6 and cont3 > cont1 and cont3 > cont2:
    print(f"C++, vencedor! com {cont3} e {perc3}")
elif cont4 > cont5 and cont4 > cont6 and cont4 > cont1 and cont4 > cont2 and cont4 > cont3:
    print(f"R, vencedor! com {cont4} e {perc4}")
elif cont5 > cont6 and cont5 > cont1 and cont5 > cont2 and cont5 > cont3 and cont5 > cont4:
    print(f"C, vencedor! com {cont5} e {perc5}") 
elif cont6 > cont5 and cont6 > cont4 and cont6 > cont3 and cont6 > cont2 and cont6 > cont1:
    print(f"Julia, vencedor! com {cont6} e {perc6}")  