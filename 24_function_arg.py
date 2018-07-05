#!/usr/local/bin/python3

def boas_vindas(*nomes):
    for item in nomes:
        print("Ola {} Seja bem vindo!".format(item))

    print(nomes)
    print(len(nomes))
    print(type(nomes))

boas_vindas('daniel', 'rafael', 'lucia')
