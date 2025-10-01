import random # Importa el módulo 'random', aunque actualmente no se usa, suele ser necesario para colocar minas aleatoriamente.

class Buscaminas:
	
	# El constructor de la clase. Se llama automáticamente cuando creas una instancia (un objeto) de Buscaminas.
	# Recibe dos argumentos: 'f' (filas) y 'c' (columnas) para definir el tamaño del tablero.
	def __init__(self, f, c):
		
		# Inicializa el 'tablero' real donde estarán las minas y números.
		# Crea una lista de 'f' elementos, donde cada elemento es inicialmente 'None'.
		# El propósito es que esta lista exterior contenga las filas del tablero.
		self.tablero = [None] * f
		
		# Inicializa el 'tablero_usuario', que es lo que ve el jugador.
		# También crea una lista de 'f' elementos 'None'.
		# Este tablero se usará para mostrar casillas ocultas, descubiertas o marcadas con bandera.
		self.tablero_usuario = [None] * f

		# Comienza un bucle para recorrer cada una de las 'f' filas del tablero.
		for i in range(f):
		
			# Para la fila actual (índice 'i') del tablero real, se crea la lista interior (la columna).
			# Asigna una nueva lista de 'c' ceros ([0] * c), representando una fila con 'c' columnas.
			# El '0' se usa como valor inicial para indicar que no hay mina cerca.
			self.tablero[i] = [0] * c
			
			# Hace lo mismo para el tablero que verá el usuario, inicializando todas las casillas a '0'.
			# Este '0' en tablero_usuario probablemente cambiará más adelante para representar casillas ocultas.
			self.tablero_usuario[i] = [0] * c

	# Define un método para comenzar a colocar las minas en el tablero.
	def colocarMinas(self):
		# Coloca una mina (-1) en la posición de la primera fila y primera columna (0, 0).
		# En un juego real de Buscaminas, esto se haría de forma aleatoria.
		self.tablero[0][0] = -1
		
	# Este método especial se llama cuando se usa la función 'print()' con el objeto Buscaminas.
	# Su objetivo es devolver una cadena de texto legible para mostrar el tablero.
	def __str__ (self):

		# Inicializa una cadena vacía donde se construirá la representación visual del tablero.
		contenido = ""
		
		# Inicia el bucle exterior para iterar sobre las filas del tablero real (self.tablero).
		for f in range(len(self.tablero)):
			# Inicia el bucle interior para iterar sobre las columnas de la fila actual.
			for c in range(len(self.tablero[f])):
				# Verifica si la posición actual (f, c) contiene una mina.
				if(self.tablero[f][c] == -1):
					# Si es una mina, añade la letra "M" y un tabulador (\t) a la cadena.
					contenido += ("M\t")
				else:
					# Si no es una mina, añade el número de la casilla (0, 1, 2, etc.) y un tabulador.
					contenido += str(self.tablero[f][c]) + "\t"

			# Después de recorrer todas las columnas de una fila, añade un salto de línea (\n).
			contenido += "\n"

		# Devuelve la cadena final con la representación del tablero.
		return contenido
	

# Este bloque se ejecuta solo cuando el script se corre directamente (no cuando se importa).
if __name__ == "__main__":
	# Crea una instancia (un objeto) de la clase Buscaminas.
	# Inicializa un tablero de 5 filas y 6 columnas.
	buscaminas = Buscaminas(5, 6)
	
	# Imprime el tablero inicial usando el método __str__. 
	# Muestra el tablero de 5x6 lleno de '0'.
	print(buscaminas)
	
	# Llama al método para colocar las minas (actualmente solo coloca una en la posición (0,0)).
	buscaminas.colocarMinas()
	
	# Imprime el tablero nuevamente. Ahora la posición (0,0) mostrará una 'M' (mina).
	print(buscaminas)