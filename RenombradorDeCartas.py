# Importa módulos necesarios para trabajar con archivos y rutas del sistema
import os, sys
from os.path import isfile, join
from os import listdir

# Diccionario que traduce los nombres en inglés de los símbolos de cartas a español
simbolo = {
    "clubs": "treboles",
    "diamonds": "diamantes",
    "spades": "espadas",
    "hearts": "corazones",
}

# Diccionario que traduce los nombres en inglés de las cartas especiales a sus abreviaciones
numero = {
    "king": "K",
    "ace": "A",
    "queen": "Q",
    "jack": "J",
}

# Función que renombra los archivos según un formato específico
def renombrador(solo_archivos):
    for archivo in solo_archivos:
        partes = archivo.split("_")  # Divide el nombre del archivo en partes usando "_" como separador
        if len(partes) == 3 and partes[2][0:-4] in simbolo:
            num = partes[0]  # Toma la primera parte como número o figura
            if num in numero:
                num = numero[partes[0]]  # Si es una figura, la convierte a su abreviación
            # Crea el nuevo nombre del archivo con el formato deseado
            nuevo = "{num}_de_{simbolo}.png".format(num=num, simbolo=simbolo[partes[2][0:-4]])
            print(nuevo)  # Muestra el nuevo nombre en consola
            # Renombra el archivo en el sistema
            os.rename(ruta + "/" + archivo, ruta + "/" + nuevo)

# Obtiene la ruta desde los argumentos del sistema (por ejemplo, al ejecutar el script)
ruta = sys.argv[1]

# Lista solo los archivos (no carpetas) dentro de la ruta especificada
solo_archivos = [f for f in listdir(ruta) if isfile(join(ruta, f))]

# Llama a la función para renombrar los archivos
renombrador(solo_archivos)
