carrito = []

# while True:
#     print('Hola Papu, como te va')

while True:
    opcion = input('Desea agregar un nuevo producto al carrito: (si/no)?: ')
    if opcion == 'si':
        produdcto = input('Ingresa el producto a agregar: ')
        carrito.append(produdcto)
        print(f'Cartito actual: {carrito}')
    else:
        break


