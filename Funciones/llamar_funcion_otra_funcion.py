def cuadrado(numero):
    """Esta función devuelve el cuadrado de un número"""
    return numero **2

print(cuadrado(3))

def suma_y_cuadrado(a,b):
    """
    Esta función toma dos números, los suma, y la suma la eleva al cuadrado finalmente devuelve el resultado
    Utiliza la función cuadrado() para calcular los cuadrados.
    """
    suma_resultado = a+b
    cuadrado_resultado = cuadrado(suma_resultado)
    return cuadrado_resultado

resultado_final = suma_y_cuadrado(3,4)

print( f"El resultado_final es {resultado_final}")
print( f"El resultado_final es {suma_y_cuadrado(3,4)}")