# @property - um getter em Py
# getter - um método para obter um atributo

# -----

# @property é uma propriedade de objeto, é um método
# que se comporta como um atributo.

# Geralmente é usada nas seguintes situações:
# - como getter 
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo

class Pencil:
    def __init__(self, color):
        self.set_color = color;

    @property #transforma function(method) em atribute;
    def cor(self):
        return self.set_color;
    
pencil = Pencil("Blue")

print(pencil.cor)

