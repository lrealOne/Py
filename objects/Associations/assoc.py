# Relações entre classes: associação,
# agregação e composição.

# Associação é um tipo de relação onde os
# objetos estão ligados dentro do sistema.
# É a relação mais comum entre objetos e tem
# subconjuntos como agregação e composição.
# Geralmente, temos uma associação quando um
# objeto tem um atributo que ref outro objeto.
# A associação não especifica como um objeto 
# controla o ciclo de vida de outro objeto.
# EXEMPLO:
class Writer:
    def __init__(self, name):
        self.name = name;
        self.writeTool = None;

    @property
    def tool(self):
        return self.writeTool
    
    @tool.setter
    def tool(self, tool):
        self.writeTool = tool


class WriteTool:
    def __init__(self, name):
        self.name = name;

    def write(self):
        return f'{self.name} is writing'
        
pencil = WriteTool("Pencil")
writer = Writer("Lou")
writer.tool = pencil # -> associação. (utilizando o attr setter ;).)

print(writer.tool.write())
