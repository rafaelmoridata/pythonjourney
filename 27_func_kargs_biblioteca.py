#!/usr/local/bin/python3

# biblioteca random
# https://docs.python.org/3/library/random.html
# https://www.pygame.org/news --> modulos para games

from random import choice, randint

nomes = ['daniel', 'maria', 'pedro', 'joao']

a = randint(0, 100)
print(choice(nomes), a)

# os nomes serao exibidos de forma sortida