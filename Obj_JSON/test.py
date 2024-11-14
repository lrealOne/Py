import json

pasta = "testefinal.json"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person01 = Person("Luan", 21)
person02 = Person("Ana", 20)
person03 = Person("Caio", 1)
bd = [person01.__dict__, person02.__dict__, person03.__dict__] # ou vars(person)

def dump():
    with open (pasta, "w") as archive:
        json.dump(bd, archive, ensure_ascii=False, indent=2)

dump()




