#!/usr/local/bin/python3


from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['4linux']
except Exception as e:
    print("ERRO: {}".format(e))


lista = []

while True:
    id_fruta = input("digite o id da fruta: ")
    nome_fruta = input("digite o nome da fruta para inserir ou 'sair': ")
    if nome_fruta == 'sair':
        break
    
    db.frutas.insert({'_id': id_fruta, 'nome_fruta': nome_fruta})


mong_leitura = db.frutas.find()
mong_leitura = [x for x in mong_leitura]
print(mong_leitura)