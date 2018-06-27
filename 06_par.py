#!/usr/bin/python3
'''
Ler numero e verificar se ele é par ou impar
e adicionar ele em uma lista com o resultado

[2, 'par']
[3, 'impar']
'''

numeros = [int(x) for x in input().split()]

print(numeros[:])

for x in numeros:
    if x % 2 == 0:
        print(x, ' - par')
    else:
        print(x, ' - impar')
