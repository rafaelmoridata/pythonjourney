#!/usr/local/bin/python3

from datetime import datetime

users = ['daniel', 'pedro', 'maria', 'joao']
cont = 0

while True:
    try:
        num = input('''
        USER
        0 - daniel
        1 - pedro
        2 - maria
        3 - joao
        S - Sair ''')
        if num.lower() == 's':
            break
        num = int(num)
        print("O usuario {} esta logado!".format(users[int(num)]))
    except IndexError as e:
        d = datetime.now()
        with open('17_library.log', 'a') as arquivo:
            result = "{}, {}".format(e, d.strftime("%Y-%m-%d %H:%M"))
            arquivo.write(result)
        break
    except KeyboardInterrupt as e:
        d = datetime.now()
        with open('17_library.log', 'a') as arquivo:
            result = "{}, {}".format(e, d.strftime("%Y-%m-%d %H:%M"))
            arquivo.write(result)
        break
    except KeyboardInterrupt as e:
        d = datetime.now()
        with open('17_library.log', 'a') as arquivo:
            result = "{}, {}".format(e, d.strftime("%Y-%m-%d %H:%M"))
            arquivo.write(result)
        break
