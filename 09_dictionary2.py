#!/usr/bin/python3

# dicionario com chave e valor, 
# percorrer só chave, só valor, ou chave e valor

import pprint

pessoas = [
    {'nome': 'rafael', 'idade': 34},
    {'nome': 'joao', 'idade': 40},
    {'nome': 'rubia', 'idade': 30},
    {'nome': 'jota', 'idade': 25},
    {'nome2': 'jeff', 'idade': 20}
]

print(type(pessoas[0])) # exibe o tipo
print(pessoas[0]) # exibe o dicionario inteiro
print(pessoas[0]['idade']) # exibe apenas a chave idade
print(pessoas[4]['nome2']) # exibe apenas a chave idade
print(pessoas[0].get('nome')) # busca uma chave na posicao 0 do dicionario, achou
print(pessoas[0].get('nome3')) # retorna none pq ñ tem a chave nome3 na posicao 0
print(pessoas[0].get('nome3')) # retorna none pq ñ tem a chave nome3 na posicao 0
print(pessoas[0].keys()) # achar as chaves
print(pessoas[0].items()) # achar os valores

