productos = { 'Computador': 800,  'Disco': 100, 'Tarjeta': 1200}
print(productos)

nuevos_productos = {'Disco': 180, 'Teclado':30}
print(nuevos_productos)

productos.update(nuevos_productos)
print(productos)

productos.pop('Tarjeta')
print(productos)

productos.update( {'Animal': 250})
print(productos)