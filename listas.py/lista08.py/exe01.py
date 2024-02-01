frase1 = input("digite uma frase: ")   
frase2 = input("digite outra frase: ")

print(f"frase 1: {frase1} e frase 2: {frase2}")  

if len(frase1) == len(frase2):
    print("a frase 1 tem o mesmo comprimento da 2")
else:
    print("a frase 1 não tem o mesmo comprimento da frase 2") 

if frase1 == frase2:
    print("a frase 1 é igual a frase 2")
else:
    print("a frase 1 não é igual a frase 2") 