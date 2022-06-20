a = input().split()
try:
    x1 = (- float(a[1]) + (float(a[1]) ** 2 - 4 * float(a[0]) * float(a[2])) ** (1/2) )/(2 * float(a[0]))
    x2 = (- float(a[1]) - (float(a[1]) ** 2 - 4 * float(a[0]) * float(a[2])) ** (1/2) )/(2 * float(a[0]))
    print('R1 = %0.5f' % x1)
    print('R2 = %0.5f' % x2)
except(TypeError):
    print("Impossivel calcular")
except(ZeroDivisionError):
    print("Impossivel calcular")
