#!/usr/local/bin/python3

nomes = ['daniel', 'joao', 'pedro', 'maria']

# teste 1

for nome in nomes:
    if nome == 'joao':
        continue   # qdo for joao, pula
    print(nome)

# teste 2


for nome in nomes:
    if nome == 'roberto':
        print('achei')
        break
else:
    print('nao achei')