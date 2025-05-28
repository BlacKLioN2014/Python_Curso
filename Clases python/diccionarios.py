
#diccionario -> key : valor
personas = {"Juan": 19, "Johan":14, "Mario": 54}
print(personas)
print(personas["Johan"])

id_frutas = {1: "Manzana", 2: "Perra", 3: "Uvas" }
id_frutas[2] = "Fresas"
print(id_frutas)
print(id_frutas[2])

#diccionario mixto
diccionario_mixto = {'numero': 42, 'texto': 'saludo', 'booleano': True}
print(diccionario_mixto)
print(diccionario_mixto['texto'])

diccionario_agrega ={'uno': 1, 'dos': 4}
diccionario_agrega['tres'] = 5
print(diccionario_agrega)

diccionario_elimina = {'a': 1, 'b':2, 'c': 3}
print(diccionario_elimina)
del  diccionario_elimina['b']
print(diccionario_elimina)

diccionario_anidado = {'a':{'uno': 1, 'dos': 2}, 'b': {'tres': 3, 'cuatro': 4}}
valor_a = diccionario_anidado['a']
valor_b = diccionario_anidado['b']
print(valor_a)
print(valor_b)

print(valor_a['uno'])
print(diccionario_anidado['a']['uno'])
print(diccionario_anidado['b']['cuatro'])