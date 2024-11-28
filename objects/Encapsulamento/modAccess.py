# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO POSSUI modificadores de acesso.

# MAS podemos seguir as seguintes convenções:
#   (sem underline) = public
#           pode ser usado em qualquer lugar.
#  _(um underline) = protected
#           não DEVE ser usado (chamado)
#           fora da classe ou de suas 
#           subclasses.
# __(dois underlines) = private
#           "name mangling" (desfiguração de
#           nomes) em py.
#           só deve ser usado na classe em
#           que foi declarado

class Mangling:
    def __init__(self):
        self.public = "público (pode ser usado em qualquer lugar.)"
        self._protected = "protegido (só deve ser usado dentro da classe ou em suas subclasses.)"
        self.__private = "privado (só deve ser usado dentro dessa classe.)"

    def metodoPublico(self):
        print(self.public);

    def _metodoProtected(self):
        print(self._protected);

    def __metodoPrivado(self):
        print(self.__private);

m = Mangling()
print(m.metodoPublico())
        