
class LectorDeArchivos:

	# Constructor de la clase. Intenta abrir el archivo.
	def _init_(self,nombre_archivo):
		try:
			# Intenta abrir el archivo en modo lectura ('r') con codificación UTF-8.
			self.lector = open(nombre_archivo, 'r', encoding='utf-8')
			self.esta_abierto = True # Marca el estado como abierto.
		# Captura el error si el archivo no existe.
		except FileNotFoundException as error:
			self.lector = None # El objeto lector es nulo.
			self.esta_abierto = False # Marca el estado como cerrado/fallido.
			# Informa al usuario que el archivo no fue encontrado.
			print("No se encuentra el archivo llamado", nombre_archivo)

	# Lee y devuelve la siguiente línea del archivo.
	def leer_linea(self):
		linea = None
		# Solo intenta leer si el archivo fue abierto y no se ha cerrado.
		if (self.esta_abierto and not self.lector.closed):
			linea = self.lector.readline()
		return linea # Devuelve la línea o None.
	
	# Intenta leer todo el contenido del archivo línea por línea usando un bucle.
	# NOTA: Este método tiene errores de lógica en el bucle 'while'.
	def leer_archivo_version2(self):
		archivo = None
		# Solo procede si el archivo está abierto.
		if (self.esta_abierto and not self.lector.closed):
			# Este 'readlines()' lee todas las líneas y mueve el puntero al final.
			archivo = self.lector.readlines()
			# El bucle 'while' aquí es redundante e incorrecto, ya que 'readline()'
			# después de 'readlines()' devolverá una cadena vacía ('') inmediatamente.
			# Además, la variable 'linea' no está definida antes del while, lo que
			# causaría un error NameError.
			while(len(linea) != 0): 
				archivo += linea
				linea = self.lector.readline()
		
		return archivo # Devuelve la lista de líneas leídas.
	
	# Lee y devuelve todo el contenido del archivo como una lista de líneas.
	def leer_archivo(self):
		archivo = None
		# Solo procede si el archivo está abierto.
		if (self.esta_abierto and not self.lector.closed):
			# Método más simple y estándar: lee todo y devuelve una lista.
			archivo = self.lector.readlines()
		return archivo


	def cerrar(self):
		if(self.esta_abierto):
			self.lector.close()
	

def main():
	# 1. Crear instancia: Intenta abrir el archivo del propio script.
	lector = LectorDeArchivos("LectorDeArchivos.py")
	
	
	# 2. Leer: Imprime el resultado de la función 'leer_archivo_version2'
	print(lector. leer_archivo_version2())
	
	# 3. Cerrar: Cierra el archivo.
	lector. cerrar ()


if __name__ == "__main__":
	main()