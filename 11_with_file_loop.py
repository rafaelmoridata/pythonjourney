#!/usr/local/bin/python3

# loop, pedindo nomes, adicionando dentro do arquivo até digitar sair

# opcao 1 - a cada loop, abre o arquivo novamente

with open('11_with_file_loop.txt', 'w'): pass # clean the file

while True:
    nome = input("digite um nome ou 'sair': ")
    if nome == 'sair':
        break
    else: 
        with open('11_with_file_loop.txt', 'a') as arquivo:
            arquivo.write(nome + '\n')  

# opcao 2 - abre o arq uma vez só, melhora a performance

with open('11_with_file_loop.txt', 'a') as arquivo:
    while True:
        nome = input("digite um nome ou 'sair': ")
        if nome == 'sair':
            break
        arquivo.write(nome + '\n')  
print("qualquer coisa")


