from itertools import groupby

students = [
    {"name": "Pete", "nota": "A"},
    {"name": "Mark", "nota": "B"},
    {"name": "Sara", "nota": "D"},
    {"name": "Anne", "nota": "C"},
    {"name": "Josh", "nota": "A"},
    {"name": "Mike", "nota": "C"},
    {"name": "Lucy", "nota": "B"},
    {"name": "Nate", "nota": "A"},
    {"name": "Mary", "nota": "C"}
] 

groupStudents = sorted(students, key=lambda a: a["nota"])

for student in groupStudents:
    print(student)