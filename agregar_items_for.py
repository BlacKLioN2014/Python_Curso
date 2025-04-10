carrito = []
cantidad = int(input('Ingresa la cantidad de productos que deseas agregar: '))

a = 0
for p in range(cantidad):
    a  += 1
    producto = input(f'Ingresa el producto {a} al carrito: ')
    carrito.append(producto)

print(f'items del carrito \n{carrito}')