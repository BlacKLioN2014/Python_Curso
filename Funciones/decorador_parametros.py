# Definición del decorador
def decorador_con_parametros(mensaje_antes, mensaje_despues):
    def decorador(funcion):
        def envoltura():
            print(f"{mensaje_antes}: Antes de llamar a la función")
            funcion()
            print(f"{mensaje_despues}: Después de llamar a la función")
        return envoltura
    return decorador

# uso del decorador
@decorador_con_parametros("Inicio","Fin")
def mi_funcion():
    print("Dentro de la función original")

#llamada a la función
mi_funcion()