def main():
	# Declara e inicializa la hilera de caracteres 'hilera' con el valor "Hola mundo"
	hilera = "Hola mundo"
	# Imprime la longitud (número de caracteres) de la hilera. Salida: 10
	print(len(hilera))
	# Crea una NUEVA hilera 'hilera2' que es la versión en MAYÚSCULAS de 'hilera'.
	hilera2 = hilera.upper()
	# Imprime la nueva hilera en mayúsculas. Salida: HOLA MUNDO
	print(hilera2)
	# Imprime la hilera original. Muestra que el método .upper() NO la modificó. Salida: Hola mundo
	print(hilera)
	# Crea una NUEVA hilera 'hilera3' que es la versión en minúsculas de 'hilera2'.
	hilera3 = hilera2.lower()
	# Imprime la nueva hilera en minúsculas. Salida: hola mundo
	print(hilera3)
	# Compara si 'hilera' ("Hola mundo") es IGUAL a 'hilera2' ("HOLA MUNDO"). Salida: False
	print(hilera == hilera2)
	# Compara si las versiones en mayúsculas de ambas son iguales. Salida: True
	print(hilera.upper() == hilera2.upper())
	# Busca la sub-hilera "hola" (minúsculas) dentro de 'hilera' ("Hola mundo"). 
    # Como Python es sensible a mayúsculas/minúsculas y 'h' no está, retorna -1.
	pos = hilera.find("hola")
	# Imprime la posición (-1 indica que no la encontró). Salida: -1
	print(pos)
	# Slicing (Rebanado): Extrae un fragmento de la hilera desde la posición 0 hasta (pero sin incluir) la 4.
	# Caracteres 0, 1, 2, 3 de "H o l a   m u n d o" son "Hola".
	subhilera = hilera [0:4]
	# Imprime la sub-hilera extraída. Salida: Hola
	print(subhilera)
	# **Slicing:** Extrae desde la posición 4 hasta el final. 
	# Los caracteres desde la 4 son " mundo". Salida:  mundo
	print(hilera[4::])
	# **Slicing:** Extrae desde la posición 4 hasta (pero sin incluir) el ÚLTIMO carácter (-1).
	# De " mundo", elimina la 'o'. Salida:  mund
	print(hilera[4:-1])
	# Imprime el carácter en la posición 0. Salida: H
	print(hilera[0])

	# Bucle For: Itera a través de cada carácter de la hilera 'hilera'.
	for letra in hilera:

	# Imprime cada carácter individual en una línea separada.
	print(letra)
	
	# *split():* Divide la hilera en una lista usando el espacio (" ") como separador.
	# Salida: ['Hola', 'mundo']
	print(hilera.split(" "))

	#Hola mundo
	#-> [Hola, mundo]
	# Divide la hilera en una lista usando la letra "o" como separador.
	# Salida: ['H', 'la mund', ''] (La 'o' final divide y deja una hilera vacía)
	print(hilera.split("o"))
	# Divide la hilera en una lista usando la sub-hilera "la" como separador.
	# Salida: ['Ho', ' mundo']
	print(hilera.split("la"))
	# Asigna el resultado del split (la lista ['Hola', 'mundo']) a la variable 'arreglo'.
	arreglo = hilera.split(" ")
	# Imprime la lista (el arreglo). Salida: ['Hola', 'mundo']
	print(arreglo)
	
	# **Método .join():** Une todos los elementos de la lista 'arreglo' usando una hilera vacía ('') como separador.
	# Transforma ['Hola', 'mundo'] de nuevo a "Holamundo". Salida: Holamundo
	print(''.join(arreglo))

if __name__ == "__main__":
	main()