a = float(input())
b = 0
c = 0
if a >= 0 and a <= 400:
    b = a * 0.15
    c = 15
if a >= 400.01 and a <= 800:
    b = a * 0.12
    c = 12
if a >= 800.01 and a <= 1200:
    b = a * 0.10
    c = 10
if a >= 1200.01 and a <= 2000:
    b = a * 0.07
    c = 7
if a > 2000:
    b = a * 0.04
    c = 4


print(f'Novo salario: {a + b:.2f}')
print(f'Reajuste ganho: {b:.2f}')
print(f'Em percentual: {c} %')