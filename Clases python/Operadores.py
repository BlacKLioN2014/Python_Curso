

#Operadores Logicos

#and (Y logico) con uno que sea falce ya es false, en true se tiene que cumplir todo
#or (ó logico) con uno que sea true ya es true.

# a = True
# b = False
#
# c = 5
# d = 5
# resultado = a == b or c == d
# print(resultado)

# not( negacion)

# a = True
# resultado = not a;
# print(resultado)

#Precednecia de operadores --Not es primero
# resultado = (True or False) and not False
# print(resultado)
# resultado = False or False and not True
# print(resultado)

# # Evaluacion perezosa
# a = True
# b= False
#
# resultado = a and b
# print(resultado)
#
# resultado = a or b
# print(resultado)

igual = a ==b
no_igual = a!=b
mayor_que = a > b
menor_que = a <b
mayor_o_igual_que = a>=b
menor_o_igual_que = a<=b