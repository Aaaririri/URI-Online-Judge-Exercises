valor = float(input())
print('NOTAS:')
valor_cem = valor // 100
valor = valor - valor_cem*100
print(f'{int(valor_cem)} nota(s) de R$ 100.00')
valor_cinquenta = valor // 50
valor = valor - valor_cinquenta*50
print(f'{int(valor_cinquenta)} nota(s) de R$ 50.00')
valor_vinte = valor // 20
valor = valor - valor_vinte*20
print(f'{int(valor_vinte)} nota(s) de R$ 20.00')
valor_dez = valor// 10
valor = valor - valor_dez*10
print(f'{int(valor_dez)} nota(s) de R$ 10.00')
valor_cinco = valor // 5
valor = valor - valor_cinco*5
print(f'{int(valor_cinco)} nota(s) de R$ 5.00')
valor_dois = valor // 2
valor = valor - valor_dois*2
print(f'{int(valor_dois)} nota(s) de R$ 2.00')
print('MOEDAS:')
valor_um = valor // 1
valor = valor - valor_um*1
print(f'{int(valor_um)} moeda(s) de R$ 1.00')
valor = valor * 100 
valor_cinquentaf = valor // 50
valor = valor - valor_cinquentaf*50
print(f'{int(valor_cinquentaf)} moeda(s) de R$ 0.50')
valor_vintecincof = valor // 25
valor = valor - valor_vintecincof*25
print(f'{int(valor_vintecincof)} moeda(s) de R$ 0.25')
valor_dezf = valor // 10
valor = valor - valor_dezf*10
print(f'{int(valor_dezf)} moeda(s) de R$ 0.10')
valor_cincof = valor // 5
valor = valor - valor_cincof*5
print(f'{int(valor_cincof)} moeda(s) de R$ 0.05')
print(f'{int(valor)} moeda(s) de R$ 0.01')