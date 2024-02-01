n = int(input("digite um numero: "))
b = 2
p = (b + (n/b)) / 2

while abs(b - p) > 0.0001:
    b = p 
    p = (b + (n/b)) / 2

print(f"{p:.2f}")   