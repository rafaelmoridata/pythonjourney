#!/usr/local/bin/python3

# leitura das linhas do arquivo

with open('11_with_file_frutas.txt', 'r') as arquivo:
    print(arquivo.readline()) # print da linha 0 do arq
    print(arquivo.readline()) # print da linha 1 do arq
    arquivo.seek(0) # zerou o cursor para 0 bytes
    print(arquivo.readline())        
