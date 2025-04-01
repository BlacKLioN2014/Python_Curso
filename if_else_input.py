#Solicitar al usuario su edad
edad_usuario = input('Por favor, ingresa tu edad: ')

#Convertir la entrada del usuario a un número entero
edad = int(edad_usuario)

#Verificar si la persona es mayor o no
if edad >= 18:
    print('Eres mayor de edad')
else:
    print('No eres mayor de edad')