
total_productos = 0
total_carrito = 0
productos = [{'nombre' : 'manzana', 'descripcion' : 'cultivada en la playa de tenacatita', 'precio':3},
                      {'nombre' : 'pera', 'descripcion' : 'cultivada en la playa de puerto vallarta', 'precio':2.5},
                      {'nombre' : 'zanahoria', 'descripcion' : 'cultivada en la playa de puerto peñasco', 'precio':1.5},
                      {'nombre' : 'coco', 'descripcion' : 'cultivado en tecoman', 'precio':5},
                      {'nombre' : 'mango', 'descripcion' : 'cultivada en jardin botanico', 'precio':6}]

carrito = []

while True:
    opcion = input('\nDeseas continuar comprando  (si/no): ')
    if opcion == 'si':
        print('\nLista de productos y precios: ')
        for index, producto in enumerate(productos):
            print( f'{index} : {producto['nombre']} ${producto['precio']}')
        id_producto =  int(input('\nIngrese el numero de producto, que desea agregar al carrito: '))

        #validar sin un producto existe e incrementar la cantidad
        if productos[id_producto] in carrito:
            productos[id_producto]['cantidad']  += 1
        else:
            productos[id_producto]['cantidad'] = 1
            carrito.append(productos[id_producto])

        print(f'\nProductos en el carrito actualmente: ' )
        total_productos = 0
        total_carrito = 0
        for index, producto in enumerate(carrito):
            print( f'Producto: {producto['nombre'].upper()}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}')
            cantidad = int(producto['cantidad'])
            total_productos += cantidad
            total_carrito = total_carrito + producto['precio'] * producto['cantidad']
        print(f'La cantidad de productos es {total_productos}')
        print(f'El total del carrito es ${total_carrito}')

    else:
        break

#linea final
print(f'\nProductos en el carrito :' )
total_productos = 0
total_carrito = 0
for index, producto in enumerate(carrito):
    print( f'Producto: {producto['nombre'].upper()}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}')
    cantidad = int(producto['cantidad'])
    total_productos += cantidad
    total_carrito = total_carrito + producto['precio'] * producto['cantidad']
print(f'La cantidad de productos es {total_productos}')
print(f'El total del carrito es ${total_carrito}')