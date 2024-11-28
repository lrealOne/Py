def p(*args):
    print(*args)
# Agregação é uma forma mais especializada
# de associação entre dois ou mais objetos.
# Cada objeto terá seu ciclo de vida 
# independente.
# Geralmente é uma relação de um para muitos,
# onde um objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas 
# pode se tratar de uma relação onde um objeto
# precisa de outro para fazer determinada
# tarefa.
# (existem controvérsias sobre as definições 
# de agregação)

#Classe carrinho de compras
class MarketCar:
    def __init__(self):
        self._products = []

    def priceFinal(self):
       return sum([product.price for product in self._products])
    
    def productList(self):
        p()
        for product in self._products:
            p(product.name, product.price)
        p()

    def appendProduct(self, *products):
        self._products.extend(products)

# Classe produtos no carrinho
class Product:
    def __init__(self, name, price):
        self.name = name;
        self.price = price;

car = MarketCar()
p1, p2 = Product("T-Shirt", 20), Product("Shoes", 99.9)

car.appendProduct(p1, p2)

print(car.priceFinal())