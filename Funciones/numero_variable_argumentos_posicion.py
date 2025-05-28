# def agregar(a,b):
#     return a + b
#
# # Error, por que solo se necesitan 2 parametros
# print(agregar(5,4, 5))

# Alternativa
def sumar(*args):
    suma = 0
    for numero in args:
        print(numero)
        suma += numero
    return suma

print(sumar(1,2,3,4,5,6,7,8,9,10))