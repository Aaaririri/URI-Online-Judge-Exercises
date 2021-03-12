leds = (6,2,5,5,4,5,6,3,7,6)
n = int(input())
v = 0
soma = 0
for i in range(n):
    v = input()
    for j in v:
        soma += leds[int(j)]
    print(f'{soma} leds')
    soma = 0

