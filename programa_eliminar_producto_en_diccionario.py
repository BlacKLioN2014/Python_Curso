productos = {'telefono': 500, 'disco': 120, 'tarjeta': 1200}
print(f'\n{productos}')

#Elimanar producto del diccionario
borrar_producto = input(f'Ingresa el producto a eliminar: ')
del productos[borrar_producto]
print(f'Producto eliminado correctamente. Lista actualizada \n{productos}')
