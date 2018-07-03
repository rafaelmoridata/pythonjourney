#!/usr/local/bin/python3


def write_arq(nome_arquivo, arq_content):
    try:
        with open(nome_arquivo, 'a') as arq:
            arq.writelines(arq_content)
            return True
    except Exception as e:
        return "Erro: {}".format(e)

open('19_functions_write_frutasxxx.txt', 'w').close() # clean the content


nomes = ['joao\n', 'daniel\n', 'rafael\n', 'mori\n']
write_arq('19_functions_write_frutasxxx.txt', nomes)
print(nomes)