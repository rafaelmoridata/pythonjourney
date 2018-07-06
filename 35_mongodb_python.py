#!/usr/local/bin/python3

from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['4linux']
except Exception as e:
    print("ERRO: {}".format(e))


dados = db.pessoas.find_one({'_id':2})
print(dados)

dados = db.pessoas.find({'_id':2})
print(dados)

dados = db.pessoas.find()
dados = [x for x in dados]
print(dados)



# db.pessoas.insert({'_id':5, 'nome':'joaozinho'})
db.pessoas.update({'_id':5}, {'$set': {'sobrenome':'prata'}})
db.pessoas.remove({'_id':'5'})

dados = db.pessoas.find()
dados = [x for x in dados]
print(dados)