def eliminar_duplicados(numeros):
    lista_salida = []
    for numero in numeros:
        if numero not in lista_salida:
            lista_salida.append(numero)
    return lista_salida

lista_numeros = [2,3,5,7,11,14,28,5,6,2]

print(lista_numeros)
print(eliminar_duplicados(lista_numeros))