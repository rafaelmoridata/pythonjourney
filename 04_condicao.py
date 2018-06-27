#!/usr/bin/python3

linguagem = input("Qual a melhor linguagem?")

if linguagem.strip().lower() == 'python':
    print('voce acertou')
elif linguagem.strip().lower() == 'golang':
    print('quase acertou')
else:
    print('voce errou!')