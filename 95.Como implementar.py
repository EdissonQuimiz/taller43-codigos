class EscritorDeArchivos:


	def __init__(self, archivo, agregarALFinal = False) :
		self.abrir(archivo,agregarALFinal)

	def abrir(self, archivo, agregarAlFinal):
		modo ='W'
		if (agregarAlFinal):
			modo = 'a'
		self.escritor = open(archivo, modo)

	def cerrar(self):
		self.escritor.close()

	def escribir(self, texto):
		datos_escritos = False
		if (not self.escritor.closed):
			self.escritor.write(texto)
			datos_escritos = True
		return datos_escritos


def main():
	escritor = EscritorDeArchivos("Prueba.txt", True)
	escritor.escribir("Hola mundo\n")
	escritor.cerrar()

if __name__ == "__main__":
	main()