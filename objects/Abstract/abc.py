"""
Classes abstratas - Abstract Base Class (abc)
ABCs são usadas como contratos para a definição
de novas classes. Elas podem forçar outras classes a
criarem métodos concretos por elas mesmas.
@abstractmethods são métodos que não tem corpo.
As regras para classes abstratas com métodos 
abstratos com método abstratos é que elas NÃO PODEM
ser instanciadas diretamente.

Metodos abstratos DEVEM ser implementados nas
subclasses (@abstractmethod).

Uma classe abstrata em Py tem sua metaclasse sendo
ABCMeta.

É possivel criar @property, @setter, @classmethod,
@staticmethod e @method como abstratos, para isso use
@abstractmethod como decorator mais interno.
"""

from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self.name = name;

    @property
    def name(self):
        ...

    @name.setter
    def name(self, value):
        self.name = value


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        print("useless")
    
        