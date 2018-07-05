#!/usr/local/bin/python3
# args

def boas_vindas(**kargs):
    print(kargs)

boas_vindas(nome='daniel', sobrenome='prata')



def boas_vindas2(**kargs):
    print(kargs)
    print("Ola meu nome é {}, sobrenome {}, tenho {} anos...".format(kargs['nome'], kargs['sobrenome'], kargs['idade']))

boas_vindas2(nome='daniel', sobrenome='prata', idade=34)
