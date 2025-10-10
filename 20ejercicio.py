def desencriptar(lista):
    # Diccionario de mapeo inverso: número (como string) a vocal
    mapeo_inverso = {
        '1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u',
        '6': 'A', '7': 'E', '8': 'I', '9': 'O', '0': 'U'
    }
    
    mensajes_desencriptados = []
    
    # Itera sobre cada mensaje encriptado en la lista de entrada
    for mensaje_encriptado in lista:
        mensaje_desencriptado = ""
        # Itera sobre cada carácter del mensaje encriptado
        for caracter in mensaje_encriptado:
            # Verifica si el carácter es un número que debe ser desencriptado
            if caracter in mapeo_inverso:
                # Si es un número, reemplaza por la vocal (mayúscula o minúscula)
                mensaje_desencriptado += mapeo_inverso[caracter]
            else:
                # Si no es uno de los números clave (consonantes u otros caracteres), 
                # mantiene el carácter original
                mensaje_desencriptado += caracter
        
        # Agrega el mensaje transformado a la lista de resultados
        mensajes_desencriptados.append(mensaje_desencriptado)
        
    return mensajes_desencriptados

# --- Ejemplos de Prueba ---
entrada_1 = ["H4l1", "M9ND0"] # Usando la O y U mayúsculas del ejemplo original (MUNDO)
resultado_1 = desencriptar(entrada_1)
print(f"Entrada Encriptada: {entrada_1}")
print(f"Salida Desencriptada: {resultado_1}")
# Salida esperada: ['Hola', 'MUNDO']

# ---
print("---")
