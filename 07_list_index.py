#!/usr/bin/python3

# lista.append(nome) --> adiciona o nome do final da lista
# lista.pop(0) --> remove o primeiro valor da lista
# lista.pop(-1) --> remove o último valor da lista
# lista.pop() --> remove o último valor da lista
# lista.remove('teste') --> remove a string "teste"
# len(nome) --> 
# lista.insert(0, 'luciano') --> insere luciano na primeira posicao
# lista.reverse() --> inverte as posicoes
# lista.sort() --> ordena
# lista.count() --> count do numero de valores na lista

lista = []

while True:
    nome = input("digite um nome ou 'sair': ")
    if nome == 'sair':
        break
    lista.append(nome)    
#random.index([3, 4])

print lista.index([3])
#lista.index(1)
#print(lista.index[3])
#lista.index()