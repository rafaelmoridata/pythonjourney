#!/usr/local/bin/python3

fruta = {'nome':'laranja', 'valor':5.55, 'qtd':26}

# com funcao anonima lambda, em apenas uma linha é possível fazer coisas simples, 
# porem não é recomendado para coisas complexas, depois fica dificil a manutencao e entendimento
var = lambda x, y: x * y
print(var)

# abaixo o mesmo código, porém, com função comum
def somar(x, y):
    return x + y

print(var(fruta['valor'], fruta['qtd']))


