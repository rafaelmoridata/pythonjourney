#!/usr/local/bin/python3

import psycopg2

try:
    con = psycopg2.connect('host=localhost dbname=projeto\
           user=Mori port=5432')
    cur = con.cursor()       
    #cur.execute("ALTER USER public SET search_path = public;")
    cur.execute("select * from pessoas")
#    cur.execute("SELECT table_name FROM information_schema.tables")
    conteudo = cur.fetchall()
    print(conteudo)
    print('conectado com sucesso!')
except Exception as e:
    print('Erro conexao: {}'.format(e))

