x=float(input("Digite o valor 1"))
y=float(input("Digite o valor 2"))

def soma_valores(x,y):
    resp = x + y 
    return resp
valor= soma_valores(x,y)
print(f"a resposta da soma de {x} + {y}={valor}")