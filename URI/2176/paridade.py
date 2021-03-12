# -*- coding: utf-8 -*-
s = input()
num_aux = s
soma = 0
for i in range(len(num_aux)):
    if num_aux[i] == '1':
        soma += 1


if soma%2 == 0:
    s += '0'
else:
    s += '1'

print(s)