#introdução json module;


import json

# person = {
#     "name": "Luan",
#     "lastname": "Carvalho",
#     "adress": [
#         {"road": "R1", "number": 32},
#         {"road": "R2", "number": 55}
#     ],
#     "height": 1.7,
#     "dev": True,
#     "Nothing": None,
# }

# with open("jsonArchive.json", "w", encoding="utf8") as archive:
#     json.dump(person, archive);

with open("jsonArchive.json", "r", encoding="utf8") as archive:
    person = json.load(archive);
    print(person)