def encriptar(lista):
    """
    Encripta una lista de mensajes reemplazando vocales por números.

    Reglas de encriptación:
    a -> 1, e -> 2, i -> 3, o -> 4, u -> 5
    A -> 6, E -> 7, I -> 8, O -> 9, U -> 0
    """
    
    # Diccionario de mapeo para la encriptación de vocales
    mapeo = {
        'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5',
        'A': '6', 'E': '7', 'I': '8', 'O': '9', 'U': '0'
    }
    
    mensajes_encriptados = []
    
    # Itera sobre cada mensaje en la lista de entrada
    for mensaje in lista:
        mensaje_encriptado = ""
        # Itera sobre cada carácter del mensaje
        for caracter in mensaje:
            # Verifica si el carácter es una vocal en el mapeo
            if caracter in mapeo:
                # Si es una vocal, reemplaza por el valor del mapeo (el número)
                mensaje_encriptado += mapeo[caracter]
            else:
                # Si no es una vocal, mantiene el carácter original
                mensaje_encriptado += caracter
        
        # Agrega el mensaje transformado a la lista de resultados
        mensajes_encriptados.append(mensaje_encriptado)
        
    return mensajes_encriptados

# --- Ejemplos de Prueba ---
entrada_1 = ["Hola", "MUNDO"]
resultado_1 = encriptar(entrada_1)
print(f"Entrada: {entrada_1}")
print(f"Salida: {resultado_1}")
# Salida esperada: ['H4l1', '90nd4'] (Nota: La O de MUNDO es mayúscula, va a '9')

print("---")

entrada_2 = ["Aeropuerto", "Comunicacion", "Secreto"]
resultado_2 = encriptar(entrada_2)
print(f"Entrada: {entrada_2}")
print(f"Salida: {resultado_2}")
# Salida esperada: ['72r4p52rt4', 'C4m5n3c1c34n', 'S2cr2t4']