
def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")

#Ejemplo de usu
imprimir_info(
    nombre="Juan",
    edad=30,
    ciudad = "Guadalajara",
    pais = "Mexico"
)

# Numeró variable de argumentos de palabra clave