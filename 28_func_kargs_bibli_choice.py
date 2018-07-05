#!/usr/local/bin/python3

from random import choice

def nomes_sorted(*sorteio):
    return choice(sorteio)
    #print(choice(args))


a = nomes_sorted('daniel', 'joao', 'rafael', 'rubia', 'debora')
print(a)

with open('28_func_kargs_bibli_choice.txt', 'r') as arq:
    pessoas = arq.readlines()
    print(choice(pessoas))