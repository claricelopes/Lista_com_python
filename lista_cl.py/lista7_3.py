mensagem = []
mensagem.append(input("digite os numeros: ")) 
mensagem_final = [] 

letras = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26] 

for i in mensagem: 
    if i in numeros: 
        indice = numeros.index(i)
        mensagem_final.append(letras[indice]) 

print(mensagem_final) 