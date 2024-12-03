# Exercicio com classes
# 1 - Criar Classe Carro (nome);
# 2 - Criar Classe Motor (nome);
# 3 - Criar Classe Fabricante (nome);
# 4 - Fazer a ligação entre Carro tem Motor;
# Obs.: Um motor pode ser de varios carros
# 5 - Fazer a ligação Carro e Fabricante
# Obs.: Um fabricante pode ter vários carros;
# Exibir o nome do carro, motor e fabricante

# Criação Classe Carro
class Car:
    def __init__(self, name):
        self.name = name    #nome do carro
        self.branch = None  #fabricante 
        self.engine = None  #motor do carro
    
    @property
    def carEngine(self):
        return self.engine
    
    @carEngine.setter
    def carEngine(self, value):
        self.engine = value 

    @property
    def carBranch(self):
        return self.branch
    
    @carBranch.setter
    def carBranch(self, value):
        self.branch = value 


    

#Criação Classe Fabricante
class Branch:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def made(self, car):
        self.cars.append(car)
    
    def listCars(self):
        print(f"\nCarros {self.name}")
        for car in self.cars:
            print(f"Modelo: {car.name}, Motor: {car.engine.model}")


#Criação da Classe Motor
class Engine:
    def __init__(self, model):
        self.model = model


#Carros
jetta= Car("Jetta") 
a3 = Car("A3")
golf = Car("Golf")

#Fabricantes
volks = Branch("Volkswagen")
audi = Branch("Audi")

#Motor
ea888 = Engine("EA888")

jetta.carEngine = ea888 #Carro tem Motor
a3.carEngine = ea888 #Carro tem Motor
golf.carEngine = ea888 #Carro tem Motor

jetta.branch = volks #carbranch
golf.branch = volks #carbranch
a3.branch = audi #carbranch

volks.made(jetta) #Fabricante e Carro
volks.made(golf) #Fabricante e Carro
audi.made(a3) #Fabricante e Carro

#listando pela fabricante:
volks.listCars()
audi.listCars()

print()

#listando pelo carro:
print(jetta.name, jetta.engine.model, jetta.branch.name)
