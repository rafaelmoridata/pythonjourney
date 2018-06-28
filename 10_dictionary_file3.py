#!/usr/bin/python3

frutas = [
    {'fruta':'goiaba', 'preco':2.0, 'qtd': 10},
    {'fruta':'atemoia', 'preco':2.5, 'qtd': 5},
    {'fruta':'laranja', 'preco':5.5, 'qtd': 8},
    {'fruta':'mamao', 'preco':7.0, 'qtd': 190},
    {'fruta':'banana', 'preco':1.8, 'qtd': 10}
]

soma = 0

for fruta in frutas:
    soma += fruta['preco'] * fruta['qtd']
    
print('Total: {:.2f}'.format(soma))
exit()
frutas2 = []