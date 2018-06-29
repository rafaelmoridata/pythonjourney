#!/usr/local/bin/python3

# loop, pedindo nomes, adicionando dentro do arquivo até digitar sair

# opcao 1 - a cada loop, abre o arquivo novamente

with open('11_with_file_index.txt', 'w'): pass # clean the file

while True:
    nome = input("digite um nome ou 'sair': ")
    if nome == 'sair':
        break
    else: 
        with open('11_with_file_index.txt', 'a') as arquivo:
            arquivo.write(nome + '\n')  

# opcao 2 - abre o arq uma vez só, melhora a performance

with open('11_with_file_index.txt', 'r') as arquivo:
    var = arquivo.readlines()
alterado = []
cont = 1
for linha in var:
    alterado.append('{}-{}'.format(cont, linha))
    cont += 1

with open('11_with_file_index2.txt', 'a') as arquivo:
    for linha in alterado:
        arquivo.write(linha)

with open('11_with_file_index2.txt', 'w'): pass # clean the file

# adiciona o número sequencialmente no final da linha
for linha in var:
    linha = linha.replace('\n', '-{}\n'.format(cont))
    alterado.append(linha)
    cont += 1
print(alterado)

with open('11_with_file_index2.txt', 'w') as arquivo:
    for linha in alterado:
        arquivo.write(linha)
    
