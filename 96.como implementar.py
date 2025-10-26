class LectorDeArchivos:

	# 1. SOLUCIÓN: El constructor debe tener doble guion bajo: __init__
	def __init__(self, nombre_archivo):
		try:
			# Intenta abrir el archivo en modo lectura ('r') con codificación UTF-8.
			self.lector = open(nombre_archivo, 'r', encoding='utf-8')
			self.esta_abierto = True
		# 2. SOLUCIÓN: La clase de excepción debe ser 'FileNotFoundError'
		except FileNotFoundError as error:
			self.lector = None
			self.esta_abierto = False
			print("No se encuentra el archivo llamado", nombre_archivo)

	def leer_linea(self):
		linea = None
		if (self.esta_abierto and not self.lector.closed):
			linea = self.lector.readline()
		return linea
	
	# 3. SOLUCIÓN: Reescrito para ser funcional. El original tenía errores de lógica y NameError.
	def leer_archivo_version2(self):
		contenido_completo = [] # Usamos una lista para guardar las líneas.
		
		if (self.esta_abierto and not self.lector.closed):
			linea = self.lector.readline() # Leemos la primera línea
			
			# Iteramos hasta que 'readline()' devuelve una cadena vacía ('')
			while(linea != ''):
				contenido_completo.append(linea) # Agregamos la línea a la lista
				linea = self.lector.readline() # Leemos la siguiente línea
		
		return contenido_completo # Devuelve la lista de líneas leídas.
	
	def leer_archivo(self):
		archivo = None
		if (self.esta_abierto and not self.lector.closed):
			archivo = self.lector.readlines()
		return archivo

	def cerrar(self):
		if(self.esta_abierto and not self.lector.closed): # Agregamos verificación de cerrado para seguridad
			self.lector.close()
	

def main():
	# La instancia ahora funciona: llama a __init__ con un argumento.
	lector = LectorDeArchivos("LectorDeArchivos.py") # Asume que el script se llama así
	
	# Leemos y mostramos el contenido con la versión corregida.
	print(lector.leer_archivo_version2())
	
	lector.cerrar()

if __name__ == "__main__":
	main()