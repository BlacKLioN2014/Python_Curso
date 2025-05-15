from Funciones.return_funciones import resultado_suma


def circulo(radio):
    area = 3.14 * radio * radio
    circunferencia = 2 * 3.14 * radio
    return area, circunferencia

a, c = circulo(23)
print(f"\nEl area del circulo es: {a} y la circunferencia del circulo es: {c}")

def operacion_basicas(a,b):
    """
    Esta función retorna la suma, resta,
    multiplicación y división de dos números.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b

    # manejo de la división por cero
    if b !=0:
        division = a / b
    else:
        division = None

    # Retorno de varios parámetros
    return  suma, resta, multiplicacion, division

suma, resta, multiplica, divide = operacion_basicas(8,0)

print(operacion_basicas(8,0))

print(suma)
print(resta)
print(multiplica)
print(divide)

