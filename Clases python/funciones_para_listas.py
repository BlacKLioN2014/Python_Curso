colores = ['Amarillo', 'Azul', 'Verde', 'Rojo', 'Gris', 'Negro']
#Longitud de una lista
print(len(colores))

#insertar un nuevo Item en la posicion deseada
colores.insert(2,'Naranja')
print(colores)

#insertar un nuevo valor al final
colores.append('Sangre')
print(colores)

#Agregar una lista anidada
frutas = ['Manzada', 'Uva', 'Toronja', 'Platano']
colores.append(frutas)
print(colores)

# Agregar items directamente , sin una lista anidada
colores.extend(frutas)
print(colores)

# Eliminar elementos
colores.remove(('Platano'))
print(colores)

# Eliminar el ultimo elemento de la lista
colores.pop()
print(colores)

 # # Index: saber el indice de un item
print(colores.index('Manzada'))

puntajes = [10,9,5,6,8,9,10,4,7,]

# Valor maximo
print(max(puntajes))

# Valor minimo
print(min(puntajes))