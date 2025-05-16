def es_palindromo(palabra):
    """
    Verifica si una palabra es un palíndromo

    Arg:
    - Palabra (srt): la palabra a verificar

    Returns:
    - bool: True si es un palíndromo, False de lo contrario
    """
    palabra = palabra.lower() #convertir a minúsculas
    palabra = palabra.replace(" ", "") #Eliminar espacios en blanco
    inversa = palabra[::-1] # [inicio:fin:paso

    return  palabra == inversa

texto = ("SOLOS")
if es_palindromo(texto):
    print(f"{texto.upper()}: Es un palíndromo")
else:
    print(f"{texto.upper()}: No es un palíndromo")
