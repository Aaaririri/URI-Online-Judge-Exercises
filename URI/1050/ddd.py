ddd = ('61', '71', '11', '21', '32', '19', '27', '31')
cidades = ('Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte')
num = input()
teste = False
for i in range(len(ddd)):
    if num == ddd[i]:
        teste = True
        print(cidades[i])
if teste == False:
    print('DDD nao cadastrado')