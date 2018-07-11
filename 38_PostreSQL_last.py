1 - Mori@/Users/Mori/github/pythonjourney> brew install postgres

2 - Mori@/Users/Mori/github/pythonjourney> pg_ctl -D /usr/local/var/postgres start && brew services start postgresql
waiting for server to start....2018-07-10 19:37:05.584 -03 [50010] LOG:  listening on IPv4 address "127.0.0.1", port 5432
2018-07-10 19:37:05.584 -03 [50010] LOG:  listening on IPv6 address "::1", port 5432
2018-07-10 19:37:05.585 -03 [50010] LOG:  listening on Unix socket "/tmp/.s.PGSQL.5432"
2018-07-10 19:37:05.623 -03 [50011] LOG:  database system was shut down at 2018-07-10 19:34:29 -03
2018-07-10 19:37:05.643 -03 [50010] LOG:  database system is ready to accept connections
 done
server started
==> Successfully started `postgresql` (label: homebrew.mxcl.postgresql)


3 - Mori@/Users/Mori/github/pythonjourney> psql postgres


4 - postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 Mori      | Superuser, Create role, Create DB, Replication, Bypass RLS | {}



5 - postgres=# create database projeto owner 'Mori';
CREATE DATABASE

6 - Mori@/Users/Mori/github/pythonjourney> psql postgres -U 'Mori'
psql (10.4)
Type "help" for help.


7 -
create table pessoas(
    id serial,
    nome varchar(50),
    email varchar(50),
    idade smallint,
    telefone varchar(12)
);

8 - postgres=# \dt
        List of relations
 Schema |  Name   | Type  | Owner 
--------+---------+-------+-------
 public | pessoas | table | Mori
(1 row)


9 - 
postgres=# insert into pessoas(nome, email, idade, telefone) values ('Rafael Mori', 'rafa@gmail.com', 30, '98370-7777');
INSERT 0 1
postgres=# insert into pessoas(nome, email, idade, telefone) values ('Maitê', 'maite@gmail.com', 2, '98370-7778');
INSERT 0 1


10 - postgres=# select * from pessoas;
 id |    nome     |      email      | idade |  telefone  
----+-------------+-----------------+-------+------------
  1 | Rafael Mori | rafa@gmail.com  |    30 | 98370-7777
  2 | Maitê       | maite@gmail.com |     2 | 98370-7778
(2 rows)


11 - 