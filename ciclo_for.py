
for numeros in range(5):
    print(numeros)

print('---------------------------------------------------------')

for numeros in range(1,100,5):
        print(numeros)

print('---------------------------------------------------------')

frutas = ['Manzana', 'Banana', 'Cereza']
for fruta in frutas:
    print(fruta)
    print(fruta)

print('---------------------------------------------------------')

mensaje = 'UnaArañaPatona'
for letra in mensaje:
    print(letra)

print('---------------------------------------------------------')

colores = ['Rojo', 'Verde', 'Azul']
for indice, color in enumerate(colores):
    print(f'Indice: {indice}, color: {color}')

print('---------------------------------------------------------')

#For anidado
for i in range(3):
    for j in range(3):
        print(f'Fila: {i},  columna: {j}')

print('---------------------------------------------------------')

#for en diccionario
estudiantes ={'nombre' : 'juan', 'edad' : 20, 'curso': 'python'}
for clave, valor in estudiantes.items():
    print(f'{clave}: {valor}')