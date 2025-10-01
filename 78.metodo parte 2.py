import random 
class Buscaminas: 
	# Recibe dos argumentos: 'f' (filas) y 'c' (columnas) para definir el tamaño del tablero.
	def __init__(self, f,c): 
		# Crea una lista de 'f' elementos, donde cada elemento es inicialmente 'None'.
		# El propósito es que esta lista exterior contenga las filas del tablero.
		self.tablero = [None] * f
		# Inicializa el 'tablero_usuario', que es lo que ve el jugador.
		# También crea una lista de 'f' elementos 'None'.
		# Este tablero se usará para mostrar casillas ocultas, descubiertas o marcadas con bandera.
		self.tablero_usuario = [None] * f 
		# Comienza un bucle para recorrer cada una de las 'f' filas del tablero.
		for i in range(f):
			# Rellena cada fila del tablero real con ceros (0), formando la matriz.
			self.tablero[i] = [0] * c
			# Rellena cada fila del tablero de usuario con guiones bajos ('_'), indicando casillas ocultas.
			self.tablero_usuario[i] = ['_'] * c

	# Método para colocar las minas al azar.
	def colocar_minas(self, minas): # Recibe el número de minas a colocar.
		# Bucle que se ejecuta hasta que el contador de minas llega a cero.
		while(minas > 0):
			# Elige una fila aleatoria dentro de los límites del tablero.
			fila = random.randint(0, len(self.tablero) -1)
			# Elige una columna aleatoria dentro de los límites de la fila.
			columna = random.randint(0, len(self.tablero[fila]) -1 )
			# Verifica si la casilla actual está vacía (cero).
			if (self.tablero[fila][columna] == 0):
				# Coloca la mina asignando el valor -1.
				self.tablero[fila][columna] = -1
				# Reduce el contador de minas pendientes.
				minas -= 1

	def colocar_numeros(self):
		# Lista con los desplazamientos de fila para revisar las 8 casillas vecinas.
		filas = [0, 0,-1,1,1,1,-1,-1]
		# Lista con los desplazamientos de columna para revisar las 8 casillas vecinas.
		cols =  [1,-1, 0,0,1,-1,1,-1]

		# Bucle principal: Recorre todas las filas del tablero.
		for f in range(len(self.tablero)):
			# Bucle principal: Recorre todas las columnas.
			for c in range(len(self.tablero[f])):
				# Verifica si la casilla actual es una mina (-1).
				if(self.tablero[f][c] == -1):
					# Inicializa un contador para revisar las 8 direcciones.
					contador = 0
					# Bucle while para revisar las 8 casillas vecinas.
					while(contador < 8):
						# Calcula la fila vecina usando el desplazamiento.
						nueva_fila = f + filas[contador]
						# Calcula la columna vecina usando el desplazamiento.
						nueva_columna = c + cols[contador]
						
						# Verifica si la casilla vecina está dentro de los límites del tablero (no se sale) Y
						if (nueva_fila >= 0 and nueva_fila < len(self.tablero) and
							nueva_columna >= 0 and nueva_columna < len(self.tablero[nueva_fila]) and
							# Verifica que la casilla vecina NO sea otra mina (-1).
							self.tablero[nueva_fila][nueva_columna] != -1):

							# Si es seguro, incrementa el número en la casilla vecina en 1.
							self.tablero[nueva_fila][nueva_columna] += 1

						# Pasa a la siguiente dirección vecina.
						contador += 1

	# Método principal para que el usuario haga un clic (revelar una casilla).
	def colocar_pieza(self, f,c, pierde = True): # Recibe la fila y columna del clic, y una bandera 'pierde'.
		# Listas con los desplazamientos de fila para la recursividad.
		filas = [0, 0,-1,1,1,1,-1,-1]
		# Listas con los desplazamientos de columna para la recursividad.
		cols =  [1,-1, 0,0,1,-1,1,-1]

		# Verifica que la posición del clic esté dentro de los límites del tablero.
		if (f >= 0 and f < len(self.tablero) and
			c >= 0 and c < len(self.tablero[f])):

			# Caso 1: La casilla está oculta ('_') Y es un cero (casilla vacía).
			if(self.tablero_usuario[f][c] == '_' and self.tablero[f][c] == 0):
				# Revela la casilla actual.
				self.tablero_usuario[f][c] = str(self.tablero[f][c])
				# Inicializa el contador para las 8 casillas vecinas.
				contador = 0
				# Bucle para revisar las 8 direcciones.
				while(contador < 8):
					# Calcula la fila y columna vecina.
					nueva_fila = f+filas[contador]
					nueva_columna = c + cols[contador]
					# Llamada recursiva: Llama a la función en la casilla vecina.
					pierde = self.colocar_pieza(nueva_fila,nueva_columna, False)
					# Pasa a la siguiente dirección.
					contador += 1
			# Caso 2: La casilla tiene un número de mina vecina (> 0).
			elif(self.tablero[f][c] > 0):
				# Revela la casilla y muestra el número.
				self.tablero_usuario[f][c] = str(self.tablero[f][c])
				# Indica que el jugador NO pierde (al haber revelado un número).
				pierde = False
			# Caso 3: La casilla es cualquier otra cosa (ya revelada, o una mina).
			else:
				# Revela la casilla (incluso si es la mina -1).
				self.tablero_usuario[f][c] = str(self.tablero[f][c])

		return pierde # Devuelve si el jugador perdió (True) o no (False).

	# Método especial para imprimir ambos tableros al usar 'print()'.
	def __str__ (self):
		contenido = ""
		# Bucle para imprimir el tablero REAL (donde están las 'M' y los números).
		for f in range(len(self.tablero)):
			for c in range(len(self.tablero[f])):
				if(self.tablero[f][c] == -1):
					contenido += ("M\t") # Muestra 'M' si es una mina.
				else:
					contenido += str(self.tablero[f][c]) + "\t" # Muestra el número.
			contenido += "\n" # Salto de línea.

		# Separador visual entre el tablero real y el de usuario.
		contenido += " - - Tablero Usuario \n"

		# Bucle para imprimir el tablero que el USUARIO ve (con '_' y números revelados).
		for f in range(len(self.tablero_usuario)):
			for c in range(len(self.tablero_usuario[f])):
				contenido += str(self.tablero_usuario[f][c]) + "\t" # Muestra '_' o el número revelado.
			contenido += "\n" # Salto de línea.


		return contenido # Devuelve el texto final con ambos tableros.
	
if __name__ == "__main__":
	# Crea el objeto Buscaminas con 5 filas y 6 columnas.
	buscaminas = Buscaminas(5,6)
	# Imprime el tablero inicial (todos ceros y guiones).
	print(buscaminas)
	# Coloca 3 minas al azar.
	buscaminas.colocar_minas(3)
	# Imprime el tablero con las minas ('M').
	print(buscaminas)
	# Calcula y asigna los números a las casillas vecinas de las minas.
	buscaminas.colocar_numeros()
	# Imprime el tablero con los números calculados.
	print(buscaminas)
	# Simula un clic del usuario en la casilla (0,0).
	buscaminas.colocar_pieza(0,0)
	# Imprime el tablero para mostrar el resultado del clic.
	print(buscaminas)