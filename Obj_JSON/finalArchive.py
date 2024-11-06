import json

from test import pasta, Person

with open (pasta, "r") as archive:
    persons = json.load(archive)
    p1 = Person(**persons[0])
    p2 = Person(**persons[1])
    p3 = Person(**persons[2])

print(persons)
print(p1.name, "\n", p2.name, "\n", p3.name)