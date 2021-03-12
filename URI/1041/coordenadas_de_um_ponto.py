entrada = list(map(float, input().split()))
a = entrada[0]
b = entrada[1]
if a == 0 and b == 0:
    print("Origem")
else:
    if a == 0:
        print('Eixo Y')
    if b == 0:
        print('Eixo X')
    if a > 0 and b > 0:
        print("Q1")
    if a < 0 and b < 0:
        print("Q3")
    if a > 0 and b < 0:
        print("Q4")
    if a < 0 and b > 0:
        print("Q2")