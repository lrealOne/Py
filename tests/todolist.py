import json
import os

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

def getData(lista, url):
    dados = []
    try:
        with open(url, "r", encoding="utf8") as arquivo:
            dados = json.load(arquivo)
    except:
        print("Não foi possivel carregar o arquivo")
        setData(lista)
    return dados;

def setData(lista, url):
    dados = lista
    with open(url, "w", encoding="utf8") as arquivo:
        dados = json.dump(lista, arquivo, indent=2, ensure_ascii=False)
    return dados



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

# lista = []
# deletados = []
# while len(lista) <= 10:
#     if len(lista) >= 11:
#         print("Você não pode mais adicionar itens")
#     else:
#         opcoes = [1, 2, 3, 4]
#         try:
#             escolha = int(input("Selecione uma opção:\n 1. Ver lista\n 2. Adicionar item\n 3. Excluir item\n 4. Desfazer\n"))
#         except:
#             print("Selecione uma opção disponivel")

#         if escolha in opcoes:
#             if escolha == 1:
#                 if len(lista) == 0:
#                     print("Lista não possui itens")
#                 else:
#                     print(lista)
#             elif escolha == 2:
#                 item = input("Adicionar:  ")
#                 if item in lista:
#                     print("item ja esta na lista")
#                 else:
#                     lista.append(item)
#                     print(lista)

#             elif(escolha == 3):
#                 if len(lista) > 1:
#                     print(f"Item removido: {lista[-1]}")
#                     deletados.append(lista[-1])
#                     lista.pop()
#                     print(f"lista atual: {lista}")
#                 else:
#                     print("A lista não possui itens")
            
#             else:
#                 if len(deletados) < 1:
#                     print("Não há itens para recuperar")
#                 else:
#                     print(f"Desfeita exclusão item: {deletados[-1]}")
#                     lista.append(deletados[-1])
#                     print(lista)
#         else:
#             print("Selecione uma opção disponivel")
    

#     def adicionarItem(item, lista):
#     lista.append(item)
#     return lista;

def listar(lista):
    print(*lista, sep="\n");

lista = []
deletados = []
while len(lista) < 11:
        opcoes = ["Listar", "Desfazer", "Refazer", "Parar"]
        escolha = input("Selecione um comando:\n 1. Listar \n 2. Desfazer \n 3. Refazer \n 4. Parar\n")
    
        if escolha.capitalize() in opcoes:
            if escolha.capitalize() == opcoes[0]:
                if len(lista) == 0:
                    print("Você ainda não listou nenhum item")
                else:
                    listar(lista)

            elif(escolha.capitalize() == opcoes[1]):
                os.system('cls')
                if len(lista) >= 1:
                    deletados.append(lista[-1])
                    lista.pop()
                    print("lista atual: ", *lista, sep="\n")
                else:
                    print("A lista não possui itens")
            
            elif(escolha.capitalize() == opcoes[2]):
                os.system('cls')
                if len(deletados) < 1:
                    print("Não há itens para refazer")
                else:
                    lista.append(deletados[-1])
                    listar(lista)
            
            elif(escolha.capitalize() == opcoes[3]):
                print("Encerrando...")
                break
        else:
            if len(lista) == 10:
                os.system('cls')
                listar(lista)
                print("Você não pode adicionar mais itens.")
            else:
                lista.append(escolha)
                os.system('cls')
                listar(lista)
            
'''
Forma mais eficaz de montar os comandos evitando o uso de if & else

 comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }

 comandos()
}
'''
    
# Salvando em JSON 

with open ("todo.json", "w+", encoding="utf8") as files:
    json.dump(lista, files)
    