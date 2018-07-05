#!/usr/local/bin/python3

def manipular_arquivo(nome, modo='r', conteudo=None):
    if modo == 'r':
        with open(nome, modo) as arquivo:
            return arquivo.readlines()
    elif modo == 'a':
        with open(nome, modo) as arquivo:
            arquivo.write(conteudo+'\n')
            return True


a = manipular_arquivo('23_modules_func.txt', 'r')
b = manipular_arquivo('23_modules_func.txt', 'a', 'josevaldo')
print(a)
print(b)