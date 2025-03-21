# Calcular Area de un triangulo  ( 1/2 * base * altura )

try:
    base = float(input("Ingresa la base del triangulo: "))
    altura = float(input("Ingresa la altura del triangulo: "))
    print(f"La base capturada es: {base}, la altura capturada es: {altura}")
    area = 1/2 * base * altura
    print(f"El calculo del area dio la cantidad: {area}")
except ValueError:
    print("Debes ingresar cantidades, no letras")