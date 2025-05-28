#Solicitar al usuario que ingrese su edad y si tiene una cuenta
edad = int(input('Ingresa tu edad: '))
tiene_cuenta = input('Tienes una cuenta?  (s/n): ').lower() ==  's'

print(tiene_cuenta)

#Evaluar condiciones anidadas
if edad >= 18:
    print('Eres mayor de edad')
    if tiene_cuenta:
        print('Puedes acceder a todas las funciones')
    else:
        print('Debes crear una cuenta para acceder a mas funciones')
else:
    print('No eres mayor de edad')
    if tiene_cuenta:
        print('Puedes acceder a funciones especificas')
    else:
        print('Deberias considerar crear una cuenta para mas opciones')