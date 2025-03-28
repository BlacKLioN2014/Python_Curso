productos = ['Computador', 'Tableta', 'Telefono', 'Teclado']

#Mostrar lista de productos actual
print(f'Lista actual de productos: {productos}')

#Preguntar al usuario, cual producto desea eliminar
producto_eliminar = input('Ingrese el producto a eliminar de la lista anterior: ')

#eliminar producto
productos.remove(producto_eliminar)

#Mostrar nuevamente la lista de productos actual tras eliminar uno
print(f'Lista actual de productos: {productos}')

#Funcionalidad de agregar producto
producto_agregar = input('Ingrese el producto a agregar a la lista anterior: ')
productos.append(producto_agregar)

print(f'Lista actual de productos: {productos}')