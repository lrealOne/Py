class Pencil:
    def __init__(self, color):
        self.set_color = color;

    @property #transforma function(method) em atribute;
    def cor(self):
        return self.set_color;

    @cor.setter #define a cor como o value passado pelo codigo
    def cor(self, value): # um setter padrão.
        self.color = value;


    
pencil = Pencil("Blue") 
pencil.color = "Black" #utilizando o setter esse tipo de metodo funciona