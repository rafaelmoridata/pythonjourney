#!/usr/bin/python3

num = int(input("digite um numero: "))

resultado = []
resultado.append(num)

if num % 2 == 0:
    resultado.append('par')
else:
    resultado.append('impar')

print(resultado)