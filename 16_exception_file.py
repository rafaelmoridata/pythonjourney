#!/usr/local/bin/python3

# loop, pedindo nomes, adicionando dentro do arquivo até digitar sair


# opcao 2 - abre o arq uma vez só, melhora a performance

try:
    with open('16_exception_file.txt', 'r') as arquivo:
        var = arquivo.readlines()
        alterado = []
        cont = 1
    for linha in var:
        alterado.append('{}-{}'.format(cont, linha))
        cont += 1
except FileNotFoundError as e:
    print("Arquivo nao encontrado: {}".format(e))
