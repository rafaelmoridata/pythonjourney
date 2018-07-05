#!/usr/local/bin/python3

# EXEMPLOS
# HUMANOS = Classe Pai
# Atributos = Nome, dt nasc, altura, peso
# Métodos = Andar, falar, comer, estudar
# Mulher = Classe filho que herda do humano (herança)
    # Comportamentos = engravidar
# Homem = Classe filho que herda do humano (herança) 

class Carro():
    def __init__(self, marca, modelo, ano, tanque_litros, percurso_kms):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.tanque_litros = tanque_litros
        self.percurso_kms = percurso_kms
    
    def andar(self):
        #temp = self.tanque_litros
        #self.tanque_litros -= 
        self.consumo = (self.percurso_kms / 12)
        temp = self.tanque_litros - self.consumo
        print('Seu carro consumiu {} litros de combustível do total de {} litros... Restou {} litros!'.format(self.consumo, self.tanque_litros, temp))


carro1 = Carro('Honda', 'Civic', 2016, 50, 30)
carro1.andar()

