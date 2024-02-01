str = input("digite uma palavra: ") 
str_nova = ''

for i in str:
    if str[0] == i:
        i = '#'
        str_nova = str_nova + i
    else:
        str_nova = str_nova + i

print(str_nova) 