# Parámetros por defecto
def  saludar(nombre="usuario"):
    # saluda al usuario utilizando un nombre proporcionado o 'usuario'
    print(f"Hola, {nombre}")

# Saludar sin proporcionar un nombre
saludar()

# Saludar proporcionando un nombre
saludar('Juanito')

def multiplicar(a, b=2, c=1):
    """"Multiplica tres números, con valores por defecto para b y c """
    resultado = a * b * c
    return  resultado

# Llamada proporcionando solo un argumento
print(multiplicar(5))

# Llamada proporcionando dos argumentos
print(multiplicar(3,4))

# Llamada proporcionando todos los argumentos
print(multiplicar(2,3,5))

print(multiplicar(b=100,a=5,c=3))