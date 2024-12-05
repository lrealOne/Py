# Herança simples - Relações entre cls
# Associação = usa
# Agregação = possui
# Composição = é dono de
# Herançã = É um


# -- Herança --
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed  

Don = Cat("Don", "Cat")

print(Don.breed)