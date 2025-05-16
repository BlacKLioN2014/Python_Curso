from idlelib.pyshell import restart_line

contador = 10
print(contador)

def agregar():
    contador = '30'
    print(contador)

agregar()
print(contador)

def  sumar():
    contador = 1
    print(contador)

def restar():
    contador = 2
    print(contador)

sumar()
restar()

contador_global = 0

def incrementar_contador():
    #Utilizar la palabra clave gloval para modificar la variable global