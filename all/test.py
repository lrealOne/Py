'''
Considerando duas listas de inteiros ou floats (lista a & b)
Some os valores nas listas retornando uma nova lista com os valores somados.

Use como padrão o tamanho da menor lista.

'''
a1 = [1, 2, 3, 4, 5, 6, 7]
a2 = [1, 2, 3, 4, 5]

def somaArray(b1, b2):
    rang = min(len(b1), len(b2))
    return [(a1[i] + a2[i]) for i in range(rang)]

resultado = somaArray(a1, a2)

# exemplo usado pelo professor
lista_soma = [x + y for x, y in zip(a1, a2)]

# print(resultado)

###################################

from itertools import combinations, permutations, product

## Combination = Ordem não importa - Iteravel + tamanho do grupo ex:(lista, 3);
clothes = ["shirts", "pants", "shorts"]
#print(list(combinations(clothes, 2)));


## Permutation = Ordem importa;
#print(list(permutations(clothes, 2)));


## Product = Ordem importa e repete valores únicos.
clothesInfo = [
    ["black", "white", "fantasy"],
    ["S", "M", "L"],
    ["Male", "Female", "unisex"]
]
print(*list(product(*clothesInfo)), sep="\n");