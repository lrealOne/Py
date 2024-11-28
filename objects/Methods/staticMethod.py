# @staticmethod (métodos estáticos) são inúteis em Py
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua 
# classe.

class Person:
    year = 2024

    def __init__(self, name, company):
        self.name = name
        self.company = company

    @staticmethod
    def methodst():
        return ...#É uma função qualquer, a unica direrença é que por algum motivo esta dentro de uma classe.
    