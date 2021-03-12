a,b,c = map(float, input().split())
result = 0.0
if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    result = a + b + c
    print('Perimetro = %0.1f' % result)
else:
    result = (a + b) * (c/2)
    print('Area = %0.1f' % result)