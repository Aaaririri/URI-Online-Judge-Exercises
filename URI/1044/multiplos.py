entrada = list(map(int, input().split()))
entrada.sort()
a = entrada[0]
b = entrada[1]
if a == b:
    print('Sao Multiplos')
else:
    if b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')