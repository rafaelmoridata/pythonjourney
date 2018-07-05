#!/usr/local/bin/python3

# orientação a objeto
# class = N atributos
# variavel = atributo = caracteristicas do objeto
# comportamentos = métodos
# semantico = entendimento sobre o objeto
# dunder init = 2 underlines

class Dog():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.energia = 5
    
    def latir(self):
        print('Au au!')
    
    def andar(self):
        self.energia -= 1
        #self.energia = 0
        if self.energia == 0:
            print('estou cansado, não consigo andar:{}'.format(self.energia))
        else:
            print('andando... energia:{}'.format(self.energia))

    def dormir(self):
        self.energia += 1
        print('andando... energia:{}'.format(self.energia))

dog1 = Dog('bilu', 2)
dog2 = Dog('dandara', 3)
#print(dog1.nome)
print(dog1.idade)
dog1.latir()
dog1.dormir()
dog1.dormir()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()