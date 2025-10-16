from LectorDeArchivos import LectorDeArchivos  # Importa una clase para leer el archivo de palabras secretas.
import random  # Importa el módulo random, necesario para seleccionar una palabra al azar.

class Ahorcado:
	# Constructor de la clase Ahorcado. Se llama al crear una nueva instancia.
	def __init__(self, palabra="", intentos = 5) : 
		# En Python, el constructor correcto se llama __init__ (con doble guion bajo).
		self.palabraSecreta = self.quitarAcentos(palabra.lower())  # Almacena la palabra, en minúsculas y sin acentos.
		self.palabraUsuario = "?" * len(palabra)  # Inicializa la palabra que ve el usuario (p. ej., "____" o "????").
		self.intentos = intentos  # Número de intentos que le quedan al jugador.

	# Método para quitar acentos de una palabra.
	def quitarAcentos(self, palabra):
		acentos = ["á","é","í","ó","ú","ü"]  # Lista de vocales acentuadas/diéresis.
		reemplazos = ["a", "e", "i", "o","u","u"] # Lista de vocales sin acento correspondientes.
		# Itera sobre la lista de acentos y reemplaza cada uno por su versión sin acento.
		for i in range(len(acentos) ):
			palabra = palabra.replace(acentos[i], reemplazos[i])
		return palabra  # Devuelve la palabra modificada.

	# Método para mostrar el estado actual del juego al jugador.
	def imprimirEstado(self):
		print(self.palabraUsuario)  # Muestra la palabra con las letras adivinadas y los signos de interrogación.
		print(self.palabraSecreta)  # Nota: Esto es útil para depuración, pero generalmente no se muestra en el juego real.
		print("Le quedan", self.intentos, "intentos") # Muestra cuántos intentos restantes tiene el jugador.

	# Método para solicitar al usuario que ingrese una letra.
	def pedirLetra(self):
		letra = input("Digite una letra: ")  # Pide al usuario que escriba una letra.
		return letra. lower ()  # Devuelve la letra en minúsculas.

	# Método para buscar la letra proporcionada por el usuario en la palabra secreta.
	def buscarLetra(self, letra): # El parámetro debería llamarse 'letra' (minúscula) para coincidir con la llamada.
		veces = 0  # Contador de cuántas veces aparece la letra.
		for i in range(len(self.palabraSecreta)):
			# Comprueba si la letra adivinada coincide con la letra de la palabra secreta en la posición 'i'.
			if (self.palabraSecreta[i] == letra):
				veces += 1
				# Actualiza la 'palabraUsuario' reemplazando el '?' con la letra correcta.
				# Combina la parte izquierda, la nueva letra y la parte derecha.
				self.palabraUsuario = self.palabraUsuario[ :i] + letra + self.palabraUsuario[i+1:]
		
		return veces # Devuelve el número de veces que se encontró la letra.

	# Método para determinar si el jugador ha ganado.
	def determinarSiGano(self):
		# Busca si todavía queda algún signo de interrogación ('?') en la palabra del usuario.
		# Si 'find("?")' devuelve -1, significa que no hay más '?' y, por lo tanto, ha ganado.
		return self.palabraUsuario. find("?") == - 1

	# Método principal que controla la lógica del juego.
	def jugar(self):
		# Bucle principal: continúa mientras el jugador no haya ganado Y le queden intentos.
		while(not self.determinarSiGano() and self.intentos > 0):
			self.imprimirEstado()  # Muestra el estado del juego.
			letra = self. pedirLetra()  # Pide al usuario que ingrese una letra.
			veces = self.buscarLetra(letra)  # Busca la letra en la palabra secreta.
			
			# Lógica de intentos:
			if (veces == 0):
				self.intentos -= 1 # Si la letra NO está en la palabra, se resta un intento.

		# Fin del juego: comprueba el resultado.
		if (self.intentos == 0):
			print("Perdió : (")  # Si no quedan intentos, el jugador perdió.
		else:
			print("Ganó : )")  # Si el bucle terminó y quedan intentos, significa que ganó.

# Función principal que inicializa el juego.
def main():

	lector = LectorDeArchivos("palabrasSecretas")  # Crea un lector para el archivo llamado "palabrasSecretas".
	lista_palabras = lector.leer_archivo()  # Lee todas las palabras del archivo y las guarda en una lista.
	
	# Pre-procesamiento de la lista de palabras:
	for i in range(len(lista_palabras)):
		lista_palabras[i] = lista_palabras[i].replace('\n', '')  # Elimina el salto de línea (\n) de cada palabra.

	# Selección de palabra aleatoria:
	aleatorio = int(random.random() * len(lista_palabras)) # Genera un índice aleatorio dentro del rango de la lista.
	
	# Inicialización y ejecución del juego:
	ahorcado = Ahorcado(lista_palabras[aleatorio]) # Crea una instancia de Ahorcado con la palabra seleccionada.
	ahorcado. jugar () # Llama al método 'jugar' para iniciar el juego.

if __name__ == "__main__":
	main()