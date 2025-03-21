
#Conversion de tipo de dato

#Puede ser int, float


##1
# a = input("Ingresa el primer número: ")
# b = input("Ingresa el segundo número: ")
# a = int(a)
# b = int(b)
# c = a+b
# print(c)


##2
# a = input("Ingresa el primer número: ")
# b = input("Ingresa el segundo número: ")
# c = int(a) + int(b)
# print(c)


#3
# a =int(input("Ingresa el primer número: "))
# b =int(input("Ingresa el segundo número: "))
# print(a + b)

# Intentar convertir las entradas a enteros
try:
    a= int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print(a + b)
except ValueError:
    print("Error: Debes ingresar solo números enteros, no cadenas de texto.")