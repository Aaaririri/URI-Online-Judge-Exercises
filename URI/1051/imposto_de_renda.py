x = float(input())
if  x <= 2000.00:
    print('Isento')
else:
    if x > 2000.00 and x <= 3000.00:
       imposto = (x - 2000.00)*0.08 
    if x > 3000.00 and x <= 4500.00:
        imposto = (x - 3000.00)*0.18 + 1000.00*0.08
    if x > 4500.00:
        imposto = (x - 4500.00)*0.28 + 1500.00*0.18 + 1000.00*0.08
    print('R$ %0.02f' %imposto)