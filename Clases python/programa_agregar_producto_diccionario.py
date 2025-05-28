
productos = {'telefono': 500, 'disco': 120, 'tarjeta': 1200}
print(f'\n{productos}')

#Bbtener nombre de producto y precio de nuevo producto
nuevo_producto = input(f'Ingresa el producto que quieres agregar: ')

nuevo_precio_producto = input(f'Ingresa el precio para el producto {nuevo_producto}: ')

#Agregar nuevo producto
productos[nuevo_producto] = int(nuevo_precio_producto)

print(f'Producto agregado correctamente. Lista actualizada \n{productos}')