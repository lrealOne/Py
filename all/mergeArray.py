lista01 = ["Salvador", "Ubatuba", "Belo Horizonte"]

lista02 = ["BA", "SP", "MG", "RJ"]

def unit(a1, a2):
    rang = min(len(a1), len(a2))
    return [(a1[i], a2[i]) for i in range(rang)]
        
        
print(unit(lista01, lista02), "unit")

## ouuuuu

print(list(zip(lista01, lista02)))