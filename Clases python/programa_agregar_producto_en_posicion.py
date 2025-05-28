productos = ['Computador', 'Tableta', 'Telefono', 'Teclado']

#Mostrar lista de productos actual
print(f'\nLista actual de productos: {productos}')

#inpunt nuevo producto a agregar
agregar_producto = input("\nIngresa el producto que quieres agregar: ")

#input despues de cual producto de  la lista actual deseas agregar el producto nuevo
agregar_despues_producto = input(f'\nDespues de cual producto deseas agregar el nuevo producto {agregar_producto}: ')

#averiguar la posicion o index del producto
index = productos.index(agregar_despues_producto)

print(f'\nEl indice de: {agregar_despues_producto} es {index}')

#Agregar nuevo producto en la posicion elegida
productos.insert(index+1,agregar_producto)
print(f'\nLista actual de productos: {productos}')
