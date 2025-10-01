
def calcular_sumatoria(numero):
	# la variable que guardará el resultado de la suma para esta llamada.
	resultando = 0
    
	# CASO TRIVIAL comprueba si el 'numero' es 0 (el punto final o caso base).
	if(numero == 0):
		# Si es 0, el resultado es 0. Esto detiene las llamadas infinitas.
		resultando = 0
	# CASO RECURSIVO si el 'numero' no es 0, debe seguir sumando.
	else:
		# la suma de todos los números anteriores (llamando a la función con 'numero - 1').
		resultando = numero + calcular_sumatoria(numero-1)
        
	# Devuelve el resultado de la suma al nivel de llamada anterior
	return resultando

def main():
	# Llama a la función recursiva para calcular la sumatoria de 5 (5+4+3+2+1).
	# Luego, imprime el resultado en la consola.
	print(calcular_sumatoria(5))


if __name__ == "__main__":
		main()