import random 
class Buscaminas: 
	# Recibe 'f' (filas) y 'c' (columnas) para el tamaño del tablero.
	def __init__(self, f,c):
		# Crea una lista de 'f' elementos, donde cada elemento es inicialmente 'None'.
		# El propósito es que esta lista exterior contenga las filas del tablero.
		self.tablero = [None] * f
		# Crea la lista base para el tablero que ve el usuario, también de tamaño 'f'.
		self.tablero_usuario = [None] * f 

		# Comienza un bucle para recorrer cada una de las 'f' filas del tablero.
		for i in range(f):
			# En cada fila 'i', crea una lista de 'c' ceros. Esto forma la matriz.
			self.tablero[i] = [0] * c
			# Hace lo mismo para el tablero del usuario.
			self.tablero_usuario[i] = [0] * c

	# Define el método para colocar las minas en el tablero.
	def colocar_minas(self, minas): # Recibe la cantidad de 'minas' a colocar.
		# Bucle que continúa mientras queden minas por colocar.
		while(minas > 0):
			# Genera un índice de fila aleatorio.
			fila = random.randint(0, len(self.tablero) -1)
			# Genera un índice de columna aleatorio.
			columna = random.randint(0, len(self.tablero[fila]) -1 )
			# Comprueba si la casilla elegida ya está vacía (es igual a 0).
			if (self.tablero[fila][columna] == 0):
				# Si está vacía, coloca la mina asignando el valor -1.
				self.tablero[fila][columna] = -1
				# Disminuye el contador de minas pendientes.
				minas -= 1

	def __str__ (self):
		contenido = ""
		# Inicia el bucle para recorrer todas las filas.
		for f in range(len(self.tablero)):
			# Inicia el bucle para recorrer todas las columnas de la fila actual.
			for c in range(len(self.tablero[f])):
				# Verifica si la posición actual (f, c) contiene una mina.
				if(self.tablero[f][c] == -1):
					# Si es una mina, añade la letra "M" y un tabulador (\t) a la cadena.
					contenido += ("M\t")
				else:
					# Si no es una mina, añade el número de la casilla que es 0 y un tabulador.
					contenido += str(self.tablero[f][c]) + "\t"
			# Después de recorrer todas las columnas de una fila, añade un salto de línea (\n).
			contenido += "\n"
		# Devuelve la cadena final con la representación del tablero.
		return contenido 
	

if __name__ == "__main__":
	# Crea un nuevo tablero de Buscaminas de 5x5.
	buscaminas = Buscaminas(5,5)
	# Imprime el tablero inicial (todos ceros).
	print(buscaminas)
	# Llama al método para colocar 3 minas al azar.
	buscaminas.colocar_minas(3)
	# Imprime el tablero con las 3 minas ('M') colocadas.
	print(buscaminas)