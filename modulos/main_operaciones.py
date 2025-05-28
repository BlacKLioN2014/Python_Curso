import  operaciones
# from operaciones import  suma

# Uso de la funciones del modulo operaciones
a = 10
b = 5

resultado_suma = operaciones.suma(a,b)
print(f"El resultado de la suma de {a} mas {b} es {resultado_suma}")

resultado_resta = operaciones.resta(a,b)
print(f"El resultado de la resta de {a} menos {b} es {resultado_resta}")

resultado_multiplicacion= operaciones.multiplicacion(a,b)
print(f"El resultado de la multiplicacion de {a} por {b} es {resultado_multiplicacion}")

resultado_division = operaciones.division(a,b)
print(f"El resultado de la division de {a} entre {b} es {resultado_division}")