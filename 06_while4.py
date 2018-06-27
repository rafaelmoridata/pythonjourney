#!/usr/bin/python3

nomes = ['daniel', 'joao', 'maria', 'pedro']
nomes = [nome.title() for nome in nomes]

nome = 'daniel'

print(True if nome == 'daniel' else False)

print(True if nome == 'daniel' else 'nao')