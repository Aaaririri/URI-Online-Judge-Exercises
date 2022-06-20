entrada = list(map(int, input().split()))
a = entrada[0]
b = entrada[1]
if a == b:
    print('O JOGO DUROU 24 HORA(S)')
else:
    if a > b:
        c = 24 - a + b
        print(f'O JOGO DUROU {c} HORA(S)')
    else:
        c = b - a
        print(f'O JOGO DUROU {c} HORA(S)')

