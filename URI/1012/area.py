n = tuple(map(float, input().split()))
print(n)
r = (n[0] * n[2])/2
print(f'TRIANGULO: {r:.3f}')
r = 3.14159 * n[2]**2
print(f'CIRCULO: {r:.3f}')
r = (n[0] + n[1]) * n[2]/2
print(f'TRAPEZIO: {r:.3f}')
r = n[1] ** 2
print(f'QUADRADO: {r:.3f}')
r = n[0] * n[1]
print(f'RETANGULO: {r:.3f}')

