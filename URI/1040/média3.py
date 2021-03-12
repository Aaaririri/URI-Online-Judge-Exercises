n = list(map(float, input().split()))
n[0] = n[0] * 2
n[1] = n[1] * 3
n[2] = n[2] * 4
m = sum(n)/10
print(f'Media: {m:.1f}')
if m < 5:
    print('Aluno reprovado.')
elif m >= 7:
    print('Aluno aprovado.')
else:
    print('Aluno em exame.')
    o = float(input())
    print(f'Nota do exame: {o:.1f}')
    o = (o + m)/2
    if o < 5:
        print('Aluno reprovado.')
    elif o >= 5:
        print('Aluno aprovado.')
    print(f'Media final: {o:.1f}')
