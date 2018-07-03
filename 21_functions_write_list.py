#!/usr/local/bin/python3


def write_arq(nome_arquivo, arq_content):
    try:
        with open(nome_arquivo, 'a') as arq:
            arq.writelines(arq_content)
            return True
    except Exception as e:
        return "Erro: {}".format(e)

def alterar_list(lista):
    lista1= []
    for x in lista:
        lista1.append('{}\n'.format(x))
    return lista1


#open('21_functions_write_list.txt', 'w').close() # clean the content
nomes = ['joao', 'daniel', 'rafael', 'mori']
nomes1 = []
for x in nomes:
    nomes1.append('{}\n'.format(x))

print(nomes1)
print(alterar_list(nomes))

exit()