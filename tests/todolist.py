"""
Exercicio 

todo = [] -> lista de tarefas
todo = ["fazer café"] -> adicionar fazer café
todo = ["fazer café", "caminhar"] -> adicionar caminhar 
desfazer = ["fazer café"] -> Refazer ["caminhar"]
desfazer = [] -> refazer ["caminhar", "fazer café"]
refazer = todo ["fazer café"]
refazer = todo ["fazer café", "caminhar"]
"""
on = True



def adicionarItem(item, lista):
    lista.append(item)
    return lista;

def excluiItem(lista, deletados):
    deletados.append(lista[-1])
    lista.pop()
    return lista

def desfazer(lista, deletados):
    lista.append(deletados[-1])
    return lista;

lista = []
deletados = []
while on:
    opcoes = [1, 2, 3]
    try:
        escolha = int(input("Selecione uma opção:\n 1. Adicionar item\n 2. Excluir item\n 3. Desfazer\n"))
    except:
        print("Selecione uma opção disponivel")

    if escolha in opcoes:
        if escolha == 1:
            item = input("Adicionar:  ")
            lista.append(item)
            print(lista)

        elif(escolha == 2):
            if lista.length > 1:
                print(f"Item removido: {lista[-1]}")
                deletados.append(lista[-1])
                lista.pop()
                print(f"lista atual: {lista}")
            else:
                print("A lista não possui itens")


    else:
        print("Selecione uma opção disponivel")
    
    
    