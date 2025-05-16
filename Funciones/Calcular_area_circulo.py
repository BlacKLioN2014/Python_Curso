import math


def calcular_area_circulo(radio):
    area = math.pi * radio **2
    return round(area,2)

print(calcular_area_circulo(55))

radio_circulo  = int(input("ingrese el radio: "))
area_resultante = calcular_area_circulo(radio_circulo)
print(f"Para un circulo con radio {radio_circulo}, el area es: {area_resultante}")