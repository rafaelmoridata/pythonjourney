#!/usr/bin/python3

aluno = input('Nome do aluno: ')
nota1 = float(input('Nota1: '))
nota2 = float(input('Nota2: '))
aluno1 = aluno.strip()
media = (nota1 + nota2) / 2

if media >= 7 and media <= 10:
    result = 'Aprovado'
elif media >= 6 and media <= 6.9:
    result = 'DP'
else:
    result = 'Reprovado'

print("O aluno {} tem \
        a media {} e foi {}".format(aluno, media, result))