import time;

"""
Objetos em Python

Algumas informações sobre objects podem não estar nesse arquivo, já que parti pro Python ja sabendo sobre POO em Java e JavaScript. 
"""

# Class teoria 

# Classes, em Python, são como moldes que nos permitem criar objetos. Esses objetos, então, podem conter dados (atributos) e funcionalidades (métodos). O uso de classes facilita a organização do código, tornando-o mais modular, reutilizável e fácil de entender. 
# Além disso, elas são a base da programação orientada a objetos.

# Class Prática

class Carro:
    def __init__(self, name):
        self.name = name
    
    def acelerar(self):
        print(f"{self.name} acelerou")


fusca = Carro("Fusca")

print(fusca.name)
fusca.acelerar()


class Character:
     def __init__(self, name, type, healthBarr):
         self.name = name
         self.type = type
         self.healthBarr = healthBarr

     def attack(self, damage):
         print (f"{self.name} attacks (- {damage})")

     def defence(self, damage):
         print(f"{self.name} foi atacado e se defendeu, sua barra de vida agora está em {self.healthBarr - damage}%")

itachi = Character("Itachi", "Ninja", 79)

itachi.attack(20)
itachi.defence(45)


class Camera:
    def __init__(self, modelo, filmando = False):
        self.modelo = modelo
        self.galeria = 0
        self.filmando = filmando


    def filmar(self):
        if not self.filmando:
            print(f"{self.modelo} iniciou a gravação..")
            self.filmando = True
        else:
            print(f"{self.modelo} já esta filmando...")
        
    
    def parar(self):
        if self.filmando:
            print(f"Gravação encerrada. ({self.modelo})")
            self.galeria += 1
            self.filmando = False
        else:
            print(f"{self.modelo} já está desligado")

    def fotografar(self):
        print(f"{self.modelo} tirou foto")
        self.galeria += 1

    def arquivos(self):
        print(f"{self.galeria} arquivos")

    def excluir(self):
        print(f"O ultimo arquivo foi excluido, a galeria possui {self.galeria} arquivos.")

c1 = Camera("Sony")
