a = list(map(int, input().split()))

if a[0] == a[2] and a[1] == a[3] :
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    if a[0] == a[2]:
        c = 0
        if a[1] > a[3]:
            c = 23
            d = 60 - a[1] + a[3]
        if a[1] < a[3]:
            d = a[3] - a[1]
            c = 0
    if a[0] > a[2]:
        c = 24 - a[0] + a[2]
        if a[1] > a[3]:
            c = c - 1
            d = 60 - a[1] + a[3]
        if a[1] < a[3]:
            d = a[3] - a[1]
        if a[1] == a[3]:
            d = 0
    if a[0] < a[2]:
        c = a[2] - a[0]
        if a[1] > a[3]:
            c = c - 1
            d = 60 - a[1] + a[3]
        if a[1] < a[3]:
            d = a[3] - a[1]
        if a[1] == a[3]:
            d = 0


    print(f'O JOGO DUROU {c} HORA(S) E {d} MINUTO(S)')