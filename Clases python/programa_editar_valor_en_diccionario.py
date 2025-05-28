productos = {'telefono': 500, 'disco': 120, 'tarjeta': 1200}
print(f'\n{productos}')

#Cambiar precio de un producto
producto_cambiar_precio = input(f'Ingresa el producto al cual deseas cambiarle el precio : ')
precio_nuevo = input(f'Ingresa el nuevo precio para el producto {producto_cambiar_precio}: ')

#funcionalidad cambiar valor

productos[producto_cambiar_precio] = int(precio_nuevo)
print(f'Producto actualizado correctamente. Lista actualizada \n{productos}')
