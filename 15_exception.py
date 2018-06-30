#!/usr/local/bin/python3

while True:
    try:
        num = int(input("Digite um numero: "))
        print(num)
        break
    except Exception as e:
        print("Não é um inteiro: {}".format(e))

    except ValueError as e:
        print("Não é um inteiro: {}".format(e))


