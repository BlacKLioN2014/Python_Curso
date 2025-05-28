def factorial(n):
    # Caso base: el factorial de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo: n!  = n * (n -1)!
    else:
        print(n)
        return n  * factorial(n -1)

# Ejemplo de uso
numero = 5
resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es: {resultado_factorial}")