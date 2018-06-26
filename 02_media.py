#!/usr/bin/python3
# ler o nome de um aluno
# ler duas notas e calcular a média
# mostrar a média e o nome do aluno
aluno = input("Nome do aluno: ")
nota1 = int(input('Nota1: '))
nota2 = int(input('Nota2: '))
aluno = aluno.strip()
media = (nota1 + nota2) / 2

print("O aluno {} tem \
        a media {}".format(aluno, media))