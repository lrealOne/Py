# Problema com parametros mutaveis em funções py

def addCustomer(name, list=[]):
    list.append(name)
    return list

customers1 = addCustomer("Louis")
addCustomer("Louise", customers1)

print(customers1)

customers2 = addCustomer("Mary")
addCustomer("Dave", customers2)
print(customers2)

##### como evitar esse "erro"

def addCustomerRight(name, list=None):
    if list == None:
        list = []
    list.append(name)
    return list

customers3 = addCustomerRight("Nick")
addCustomerRight("Jake", customers3)
print(customers3)

customers4 = addCustomerRight("Marie")
addCustomerRight("Diana", customers4)
print(customers4)