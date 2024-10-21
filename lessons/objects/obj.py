"""
Objetos em Python
"""

# Class

class Carro:
    def __init__(self, name):
        self.name = name
    
    def acelerar(self):
        print(f"{self.name} acelerou")


fusca = Carro("Fusca")

print(fusca.name)
fusca.acelerar()