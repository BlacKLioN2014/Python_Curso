import random
import  math

# libreria para fecha datetime
# libreria para sistema operativo os

# Generar un número entero aleatorio entre 1 y 10
numero_aleatorio = random.randint(1,10)
print(f"Número aleatorio {numero_aleatorio}")


# Obtener un elemento aleatorio de una lista
lista = [1,2,3,4,5]
elemento_aleatorio = random.choice(lista)
print("Elemento aleatorio : ", elemento_aleatorio)

# Calcular la raíz cuadrada
raiz_cuadrada = math.sqrt(25)
print("Raiz cuadrada: ", raiz_cuadrada)

# Calcular el seno de un ángulo en radianes
seno = math.sin(math.radians(90))
print("seno de 90 grados: ", seno)



