# Decoradores em py

def decoradora(func):
    print("Função Exe");
    
    def aninhada(*args, **kwargs):
        print("aninhada exe");
        res = func(*args, **kwargs)
        return res;
    return aninhada

@decoradora
def soma(x, y):
    return x + y;

print(soma(4, 5))

