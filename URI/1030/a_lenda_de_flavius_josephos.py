k_aux = int(input())
k = 0
while k != k_aux:
    x, n = map(int, input().split())
    lista = list(range(1,x+1))
    j = 0
    if x > n:
        j = n - 1
    else:
        j = n - x - 1
        while j >= len(lista):
            j = j - len(lista)
    for i in range(len(lista)-1):
        lista.pop(j)
        j = j + n - 1
        while j >= len(lista):
            j = j - len(lista)
    k = k + 1
    print(f'Case {k}: {lista[0]}')

