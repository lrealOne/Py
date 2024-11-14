import json

from test import pasta, Person, dump

with open (pasta, "r") as archive:
    data = json.load(archive)
    p1 = Person(**data[0])
    p2 = Person(**data[1])
    p3 = Person(**data[2])

print(data)
print(p1.name, "\n", p2.name, "\n", p3.name)