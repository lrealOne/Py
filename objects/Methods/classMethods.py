# Métodos de classe + factories
# métodos onde 'self' será 'cls', ou seja,
# ao invés de receber a instância no primeiro
# parametro, receberemos a propria classe.
def pprint(*objs):
    for obj in objs:
        print(*vars(obj).values(), sep=", ")

class Person:
    year = 2024

    def __init__(self, name, company):
        self.name = name
        self.company = company

    @classmethod
    def noWork(cls, name):
        return cls(name, "No company")


person01 = Person("Luan", "Google")
person02 = Person.noWork("Júlia")
pprint(person01, person02)


