#!/usr/local/bin/python3

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arq:
            return arq.readlines()
    except Exception as e:
        return "Erro: {}".format(e)

arquivo = ler_arquivo('19_functions_frutasxxx.txt')
print(arquivo)