a = [5, 6, 7]

#Mutabilidad de listas, trata de que puedo cambiar los valores de los items de una lista
print(a)

a[1] = 80
a[2] = 45
print(a)

a[0:0] = [55, 22, 36]
print(a)