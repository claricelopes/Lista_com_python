x = 70000
y = 180000
contador = 0

while (x <= y):
    x += (x * 0.035) 
    y += (y * 0.015) 
    contador += 1

print(f"numero de anos: {contador}") 