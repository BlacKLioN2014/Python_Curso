# conjunto1 = {1, 2, 3}
# conjunto2 = {3, 4, 5, 6, 7}
#
# #Union de dos conjuntos
# union = conjunto1 | conjunto2
# print(conjunto1)
# print(conjunto2)
# print(union)
#
# #Intersepcion de dos conjuntos
# interseccion = conjunto1 & conjunto2
# print(interseccion)

# #diferencia
# conjunto1 = {1, 2, 3, 5}
# conjunto2 = {3, 4, 5, 6, 7}
# diferencia = conjunto2 - conjunto1
# print(diferencia)
#
# #Diferencia simetrica de dos conjuntos
# diferencia_simetrica = conjunto1 ^ conjunto2
# print(diferencia_simetrica)

#Saber si existe un valor
# print(9 in conjunto2)

conjunto4 = {1, 2, 3}

#agregar nuevo elemento al conjunto
conjunto4.add(4)
print(conjunto4)

#remover  un elemento
conjunto4.remove(2)
print(conjunto4)

#conjunto inmutable , no se puede agregar o remover valores tras su definicion
conjunto_inmutable = frozenset([1, 2, 3])
conjunto_inmutable.remove(5)