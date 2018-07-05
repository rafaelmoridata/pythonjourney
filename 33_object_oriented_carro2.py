#!/usr/local/bin/python3

# EXEMPLOS
# HUMANOS = Classe Pai
# Atributos = Nome, dt nasc, altura, peso
# Métodos = Andar, falar, comer, estudar
# Mulher = Classe filho que herda do humano (herança)
    # Comportamentos = engravidar
# Homem = Classe filho que herda do humano (herança) 

class Car():
    """ Tentando abstrair um carro """
    def __init__(self, ano, modelo, marca):
        self.ano = ano
        self.modelo = modelo
        self.marca = marca
        self.velocidade = 0
        self.combustivel = 'gasolina'
    
    def acelerar(self):
        self.velocidade += 10
        print('acelerando...')
    
    def freiar(self):
        self.velocidade -= 10
        print('freiando....')
    
    def __str__(self):
        return 'ano:{} modelo:{}'.format(self.ano, self.modelo)

class Car_electric(Car):
    def __init__(self):
        self.combustivel = 'energia'

car1 = Car_electric()
car1.ano = 2005
car1.modelo = 'BMW'
car2 = Car(2018, 'c200', 'mercedez')

print(car1.combustivel)
print(car1.modelo)
print(car2.combustivel)
print(car2.modelo)
print(car1.__str__())

        