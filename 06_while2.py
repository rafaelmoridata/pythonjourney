#!/usr/bin/python3

soma = 0

while True:
    num = int(input("digite um numero ou 1 para sair"))
    soma += num
    if num == 1:
        break
    

print('total: {}'.format(soma))
