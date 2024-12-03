# Relações entre classes: associação, agregação e composição.
# Composição é uma especialização da agregação.
# Mas nela, quando o obj pai for apagado, todas as referencias do obj filho tambem serão.

class Customer:
    def __init__(self, name):
        self.name = name
        self.address = []

    def insertAddress(self, st, number):
        self.address.append(Address(st, number))

    def __del__(self):
        print("Delete: ", self.name)
    

class Address:
    def __init__(self, st, number):
        self.st = st
        self.number = number
        
    def __del__(self):
        print("Delete: ", self.st, self.number)


customer01 = Customer("Maria")
customer01.insertAddress("St Aruana", 72)
customer01.insertAddress("St Manoel Almeida", 66)

del(customer01)

print("It's over here.")