import unicodedata

def es_palindromo(palabra):
    # Paso 1: Normalización de la palabra

    # 1.1 Quitar acentos (Normalización Unicode)
    # NFD separa el carácter de la marca diacrítica ('é' -> 'e' + acento)
    palabra_sin_acentos = unicodedata.normalize('NFD', palabra)
    
    # Se utiliza .encode('ascii', 'ignore') para descartar la marca diacrítica
    # y .decode('utf-8') para obtener la cadena limpia
    palabra_limpia = palabra_sin_acentos.encode('ascii', 'ignore').decode('utf-8')
    
    # 1.2 Normalizar a minúsculas
    palabra_final = palabra_limpia.lower()
    
    # Paso 2: Verificar si es un palíndromo
    
    # Comparar la palabra normalizada con su reverso.
    # [::-1] es la sintaxis de Python para invertir una cadena.
    return palabra_final == palabra_final[::-1]

# --- Ejemplos de Prueba ---
print(f"'{'Ana'}' es palíndromo: {es_palindromo('Ana')}")         # True (ana == ana)
print(f"'{'aérea'}' es palíndromo: {es_palindromo('aérea')}")     # True (aerea == aerea)
print(f"'{'erigiré'}' es palíndromo: {es_palindromo('erigiré')}") # True (erigire == erigire)
print(f"'{'radar'}' es palíndromo: {es_palindromo('radar')}")     # True (radar == radar)
print(f"'{'Python'}' es palíndromo: {es_palindromo('Python')}")   # False (python != nohtyp)