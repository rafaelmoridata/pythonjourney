#!/usr/bin/python3

>>> pessoa = {}
>>> pessoa = {'nome': 'daniel', 'email':'dani@gmail.com'}
>>> pessoa['nome']
'daniel'
>>> pessoa['email']
'dani@gmail.com'



>>> pessoa = {'nome': 'daniel', 'email':'dani@gmail.com'}
>>> for x in pessoa.keys():
...     print(x)
...     
... 
email
nome
>>> for x in pessoa.values():
...     print(x)
...     
... 
dani@gmail.com
daniel


>>> for x in pessoa.items():
...     print(x)
...     
... 
('email', 'dani@gmail.com')
('nome', 'daniel')



