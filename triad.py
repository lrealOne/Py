from functools import partial

### Map 

products = [
    {"name": "Apple", "price": 10.00},
    {"name": "Banana", "price": 12.00},
    {"name": "Orange", "price": 8.00},
    {"name": "Cherry", "price": 18.00},
    {"name": "Watermelon", "price": 14.00}
];


    
productsNewPrice = map(lambda x: round(x["price"] * 1.1, 2), products)

#print(list(productsNewPrice))

### Filter 

def filterP(product, value):
    return product["price"] > value;

newProducts = filter(lambda product: filterP(product, 10), products)

#print(list(newProducts))

## Reduce
from functools import reduce;

def reduceP(a, p):
    return a + p["price"];

print(reduce(reduceP, products, 0))