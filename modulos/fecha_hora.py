import datetime
# from datetime import  datetime

# obtener la fecha y la hora actual
ahora = datetime.datetime.now()
print("Fecha y hora actual: ", ahora)

#formatear la fecha y hora como una cadena
formato = " %Y-%m-%d %H:%M:%S"
cadena_formateada = ahora.strftime(formato)
print(F"Fecha y hora formateada:  {cadena_formateada}")