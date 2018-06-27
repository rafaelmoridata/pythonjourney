#!/usr/bin/python3

'''
lista de nome vazia
ler nomes, adicionar na lista ate digitar sair
'''

lista = []

while True:
    nome = input("digite um nome ou 'sair': ")
    if nome == 'sair':
        break
    lista.append(nome)    

print(lista)