#!/usr/local/bin/python3
# kargs

#{'fruta':'laranja', 'preco':2.0, 'qtd': 10}

def valor_total(**frutas):
    return frutas['preco'] * frutas['qtd']
    
a = valor_total(preco=5, qtd=50) 
print(a)