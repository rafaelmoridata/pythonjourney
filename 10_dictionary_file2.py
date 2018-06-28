#!/usr/bin/python3

cont = 0

frutas = [
    {'fruta':'goiaba', 'preco':2.0},
    {'fruta':'atemoia', 'preco':2.5},
    {'fruta':'laranja', 'preco':5.5},
    {'fruta':'mamao', 'preco':7.0},
    {'fruta':'banana', 'preco':1.8}
]

frutas2 = []

for fruta in frutas:
    fruta['preco'] = fruta['preco'] + 0.5 # fruta['preco'] += 0.5 tb funciona
    frutas2.append(fruta)
    
print(frutas2)

