#Solicitar al usuario, que ingrese una calificación
entrada_usuario = input("Ingresa tu calificación: ")
calificacion  = float(entrada_usuario)

#Evaluar calificacion
if calificacion >= 90:
    print('Calificacion: A')
elif calificacion >= 80:
    print('Calificacion: B')
elif calificacion >= 70:
    print('Calificacion: C')
elif calificacion >= 60:
    print('Calificacion: D')
else:
    print('Calificacion: F (Reprobado)')