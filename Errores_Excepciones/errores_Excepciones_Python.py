
# numero_random = int(input ("¿Dame un numero? "))
# for numero in range(1,numero_random):
#     if  float(numero/2 ).is_integer():
#         print(f"El numero {numero} es par")
#     else:
#         print(f"El numero {numero} es impar")


# def ejercicio(a, b):
#     return a * b
# numero_uno= int(input ("¿Dame un primer numero? "))
# numero_dos= int(input ("¿Dame un segundo numero? "))
# resultado =ejercicio(numero_uno,numero_dos)
# print(f"El resultado de la multiplicación es: {resultado}")


# try:
#     num = int(input("Ingresa un número: "))
#     print(10 / num)
# except ValueError:
#     print("Eso no es un número válido")
# except ZeroDivisionError:
#     print("No puedes dividir entre cero")


# try:
#     num = int(input("Ingresa un número: "))
# except ValueError:
#     print("No es un número válido")
# else:
#     print("Ingresaste el número:", num)


# try:
#     archivo = open("archivo.txt")
# except FileNotFoundError:
#     print("El archivo no existe")
# finally:
#     print("Esto se ejecuta siempre")


# try:
#     valor = int(input("Ingresa un número: "))
#     print(10 / valor)
# except Exception as e:
#     print("Ocurrió un error:", e)


# try:
#
#     num_uno = int(input ("¿Dame un primer numero? "))
#     num_dos = int(input ("¿Dame un segundo numero? "))
#     division = num_uno / num_dos
#     print(f"El resultado de la división de los numeros ingresados es {division}")
# except ValueError:
#     print("Debes ingresar números válidos")
# except ZeroDivisionError:
#     print("No se puede dividir entre cero")
# except exception as e:
#     print(f"Ocurrió el siguiente error: {e}")
# finally:
#     print("Programa terminado")


# peliculas = ["Dune", "Interestellar", "Hashiko", "Talk to me", "El perfume"]
# peliculas.append("Gataca")
# peliculas.insert(2,"Depredador")
# for pelicula in peliculas:
#     tamaño = len(pelicula)
#     if tamaño > 5:
#         print(f"La pelicula {pelicula} tiene mas de 5 caracteres")


# agenda = {
#     "Abraham":{"nombre" : "abraham", "edad" : 33, "ciudad": "Guadalajara"},
#     "Marcos":{"nombre" : "marcos", "edad" : 33, "ciudad": "Zapopan"},
#     "Anco":{"nombre" : "anco", "edad" : 26}
# }
# for clave, valor in agenda.items():
#     print(f"Nombre: {valor.get("nombre", "Desconocido")}, Edad: {valor.get("edad", 20)}, Ciudad: {valor.get("ciudad", "El salto")}")


# nombre = input("Ingresa tu nombre completo: ")
# print(nombre.upper())
# print(nombre[0])
# contador= 0
# for caracter in nombre:
#     if not caracter.isspace():
#         contador += 1
# print(f"El nombre {nombre} tiene: {contador} caractereres, no se contaron espacios")


# texto = 'Tigres vendio el partido del pasado sabado.'
# patron = re.compile(r"vendio")
# resultado = patron.search(texto)
#
# if resultado:
#     print("Encontrado: ", resultado.group())


# texto = "uno dos tres dos"
# patron = re.compile(r"dos")
# coincidencias = patron.findall(texto)
# resultado = patron.search(texto)
# print(coincidencias)  # ['dos', 'dos']
# print(resultado.group())


# texto = "Teléfono: 123-456-7890"
# patron = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
# resultado = patron.search(texto)
# if resultado:
#     print("Código área:", resultado.group(1))
#     print("Número:", resultado.group(2), resultado.group(3))

#
# import re
# texto = "Mi correo es abraham@mail.com y el de trabajo es trabajo@empresa.com"
# patron = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}")
# correos = patron.findall(texto)
# print(correos)


# import re
# patron = re.compile(r"Hola")
# print(patron.match("Hola mundo"))  # Coincide al inicio
# print(patron.search("Mundo Hola")) # Busca en toda la cadena


# import re
# texto = "Mi número es 123-456-7890"
# patron = re.compile(r"\d{3}-\d{3}-\d{4}")
# nuevo_texto = patron.sub("XXX-XXX-XXXX", texto)
# print(texto)
# print(nuevo_texto)


# import re
# patron = re.compile(r"python", re.IGNORECASE)
# print(patron.search("PYTHON es genial"))


# import re
# texto = "Contactos: Ana 555-123-4567, Juan 555-765-4321"
# patron = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
# resultado = patron.search(texto)
# for match in patron.finditer(texto):
#     print("Código área:", resultado.group(1))


# archivo = open("C:\\Users\\abraham.jimenez\\Desktop\\Git.txt", "r")  # "r" = leer
# contenido = archivo.read()
# print(contenido)
# archivo.close()


# archivo = open("C:\\Users\\abraham.jimenez\\Desktop\\Git.txt", "r")  # "r" = leer
# for linea in archivo:
#     print(linea.strip())  # .strip() quita saltos de línea
# archivo.close()


# with open("C:\\Users\\abraham.jimenez\\Desktop\\Git.txt", "r") as archivo:
#     contenido = archivo.read()
#     print(contenido)


# with open("C:\\Users\\abraham.jimenez\\Desktop\\galleta.txt", "w") as archivo:  # "w" = sobrescribir
#     # archivo.write("Hola, Abraham\n")
#     # archivo.write("Aprendiendo Python con todo \n")
#     archivo.write("Hola, pepe\n")
#     archivo.write("Como te va \n")


# with open("C:\\Users\\abraham.jimenez\\Desktop\\galleta.txt", "a") as archivo:  # "a" = agregar
#     archivo.write("Nueva línea agregada\n")


# with open("C:\\Users\\abraham.jimenez\\Desktop\\galleta.txt", "r") as archivo:
#     lineas = archivo.readlines()
#     print(lineas)  # ['Hola\n', 'Python\n']


# import os
# ruta = os.path.join("C:\\Users\\abraham.jimenez\\Desktop","galleta.txt")
# print(ruta)  # carpeta/archivo.txt (en Windows usa \)


# import os
# if os.path.exists("C:\\Users\\abraham.jimenez\\Desktop\\galleta.txt"):
#     print("El archivo existe")
# else:
#     print("No existe")


# with open("C:\\Users\\abraham.jimenez\\Desktop\\helado.txt", "w") as archivo:  # "w" = sobrescribir
#     # archivo.write("Hola, Abraham\n")
#     # archivo.write("Aprendiendo Python con todo \n")
#     archivo.write("Hola, pepe\n")
#     archivo.write("Como te va \n")
#     archivo.write("silo sabes \n")
# with open("C:\\Users\\abraham.jimenez\\Desktop\\helado.txt", "a") as archivo:  # "a" = agregar
#     archivo.write("verdad\n")
# archivo = open("C:\\Users\\abraham.jimenez\\Desktop\\helado.txt", "r")  # "r" = leer
# contenido = archivo.read()
# print(contenido)
# archivo.close()

# import csv
# with open("C:\\Users\\abraham.jimenez\\Desktop\\ejemplo.csv", "w", newline="") as archivo:
#     escritor = csv.writer(archivo)
#     escritor.writerow(["Nombre", "Edad", "Ciudad"])
#     escritor.writerow(["Abraham", 33, "Guadalajara"])
#     escritor.writerow(["Ana", 25, "CDMX"])


# import csv
# with open("C:\\Users\\abraham.jimenez\\Desktop\\ejemplo.csv", "r") as archivo:
#     lector = csv.reader(archivo)
#     for fila in lector:
#         print(fila)


# import csv
# with open("C:\\Users\\abraham.jimenez\\Desktop\\ejemplo.csv", "r") as archivo:
#     lector = csv.DictReader(archivo)
#     for fila in lector:
#         print(f"{fila['Nombre']} tiene {fila['Edad']} años y vive en {fila['Ciudad']}")


# import json
# persona = {
#     "nombre": "Abraham",
#     "edad": 33,
#     "ciudad": "Guadalajara"
# }
# with open("C:\\Users\\abraham.jimenez\\Desktop\\persona.json", "w") as archivo:
#     json.dump(persona, archivo)


# import json
# with open("C:\\Users\\abraham.jimenez\\Desktop\\persona.json", "r") as archivo:
#     persona = json.load(archivo)
#     print(persona["nombre"], "vive en", persona["ciudad"])


# import json
# data = '{"nombre": "Ana", "edad": 25}'
# persona = json.loads(data)  # de string a dict
# print(persona["nombre"])
# nuevo_json = json.dumps(persona)  # de dict a string
# print(nuevo_json)


# import csv
# import json
# with open("C:\\Users\\abraham.jimenez\\Desktop\\peliculas.csv", "w", newline="" , encoding="utf-8") as archivo:
#     escritor = csv.writer(archivo)
#     escritor.writerow(["Nombre", "Año", "Género"])
#     escritor.writerow(["Interestelar", 2011, "ciencia ficción"])
#     escritor.writerow(["Gattaca", 2001, "ciencia ficción"])
#     escritor.writerow(["Chucky", 1984, "horror"])
# datos = []
# with open("C:\\Users\\abraham.jimenez\\Desktop\\peliculas.csv", "r", encoding="utf-8") as archivo:
#     lector = csv.DictReader(archivo)
#     for fila in lector:
#         print(f"La película {fila['Nombre']} es del año {fila['Año']} y es del genero {fila['Género']}")
#         datos.append(fila)
#     archivo.seek(0)  # 🔥 volver al inicio
#     lector = csv.DictReader(archivo)
#     datos_ = list(lector)
# with open("C:\\Users\\abraham.jimenez\\Desktop\\peliculas.json", "w", encoding="utf-8") as archivo_json:
#     json.dump(datos, archivo_json, indent=4, ensure_ascii=False)
# with open("C:\\Users\\abraham.jimenez\\Desktop\\peliculas_.json", "w", encoding="utf-8") as archivo_json:
#     json.dump(datos_, archivo_json, indent=4, ensure_ascii=False)


# import os
# # Carpeta actual
# print("\n\nCarpeta actual:", os.getcwd())
# # Uniendo rutas de forma segura
# ruta = os.path.join("C:\\", "Users", "abraham.jimenez", "escritorio", "archiv.txt")
# print("Ruta construida:", ruta)


import os
# # Crear carpeta
# os.makedirs("Escritorio\\Carpetachuky", exist_ok=True)
# print("Carpeta creada")
# Eliminar carpeta vacía
# os.rmdir("Escritorio\\Carpetachuky")
# os.rmdir("Escritorio")
# print("Carpeta eliminada")


# import os
# # archivos = os.listdir(".")  # "." = carpeta actual
# archivos = os.listdir("C:\\Users\\abraham.jimenez\\Desktop\\Python_Curso")  # "." = carpeta actual
# print("Archivos en esta carpeta:")
# for archivo in archivos:
#     print("-", archivo)


import shutil
# # ruta donde crees que está
# ruta = r"C:\Users\abraham.jimenez\Desktop\Python_Curso\caca.txt"
# print("Existe?", os.path.exists(ruta))
# # Copiar archivo
# shutil.copy(r"C:\Users\abraham.jimenez\Desktop\Python_Curso\caca.txt", r"C:\Users\abraham.jimenez\Desktop\caca.txt")
# # Mover archivo
# shutil.move(r"C:\Users\abraham.jimenez\Desktop\Python_Curso\coco.txt", r"C:\Users\abraham.jimenez\Desktop\coco.txt")


# os.remove() → borra solo archivos.
# os.rmdir() → borra carpetas vacías.
# shutil.rmtree() → borra carpetas con todo adentro.
# import os
# # Eliminar archivo
# os.remove(r"C:\Users\abraham.jimenez\Desktop\coco.txt")
# print("Archivo eliminado")
# import shutil
# shutil.rmtree(r"C:\Users\abraham.jimenez\Desktop\Fresh")
# print("Carpeta y archivos eliminados")


