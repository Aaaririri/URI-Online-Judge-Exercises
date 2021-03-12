
a,b,c = map(float, input().split())
while(a <= b):
    if a == b and b == c:
        break
    else:
        aux = 0 
        aux = a 
        a = b 
        b = c
        c = aux


if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == (b**2 + c**2):
        print('TRIANGULO RETANGULO')
    if a**2 > (b**2 + c**2):
        print('TRIANGULO OBTUSANGULO')
    if a**2 < (b**2 + c**2):
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    if a == b != c or b == c != a or a == c != b:
        print('TRIANGULO ISOSCELES')
