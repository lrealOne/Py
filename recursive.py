# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - uteis para dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - um problema que possa ser dividido em partes menores
# - um caso recursivo que resolve o pequeno problema
# - um caso base que para a recursão
# Exemplo = fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120

def recursive(s=0, f=5):
    if s >= f:
        return f
    print(s)
    s += 1
    return recursive(s, f)

print(recursive())