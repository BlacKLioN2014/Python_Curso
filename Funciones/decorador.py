# Definición del decorador
def decorador(funcion):
    def envoltura():
        print("Antes de llamar a la función")
        funcion()
        print("Despues de llamar a la función")
    return envoltura

# uso del decorador
@decorador
def mi_funcion():
    print("Dentro de la función original")

#llamada a la función
mi_funcion()