puntajes = [2, 5, 6 ,8, 4, 10]

def agregar(numeros):
    total = 0
    for numero in numeros:
        total  += numero
    return total

print(agregar(puntajes))