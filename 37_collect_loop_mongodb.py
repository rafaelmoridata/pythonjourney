#!/usr/local/bin/python3




db.frutas.remove()
for fruta in frutas:
    a = sorteio(ids)
    ids.remove(a)
    fruta['_id'] = a
    db.frutas.insert(fruta)