
class EscritorDeArchivos:

    # Recibe el nombre del archivo y un booleano para decidir si se agrega al final.
    def __init__(self, archivo, agregarALFinal = False) :
        # Llama al método 'abrir' para inicializar la conexión con el archivo.
        self.abrir(archivo,agregarALFinal)

    # abrir(self, archivo, agregarAlFinal):
    # Método para abrir el archivo en el modo correcto.
    def abrir(self, archivo, agregarAlFinal):
        # Modo predeterminado: 'w' (write), que sobrescribe el archivo si existe.
        modo ='w'
        # Si 'agregarAlFinal' es True, cambia el modo a 'a' (append) para añadir datos.
        if (agregarAlFinal):
            modo = 'a'
        # Abre el archivo y guarda el objeto de archivo (el escritor) en 'self.escritor'.
        self.escritor = open(archivo, modo)

    # Método para cerrar la conexión con el archivo, guardando los datos pendientes.
    def cerrar(self):
        self.escritor.close()

    # Método para escribir el 'texto' en el archivo, si no está cerrado.
    def escribir(self, texto):
        datos_escritos = False
        # Verifica que el archivo no esté cerrado antes de intentar escribir.
        if (not self.escritor.closed):
            self.escritor.write(texto)
            datos_escritos = True
        # Retorna True si se pudo escribir, False si no (porque estaba cerrado).
        return datos_escritos


def main():
    # 1. Crear una instancia: Abre "Prueba.txt" en modo 'a' (append) porque 'True' es pasado.
    escritor = EscritorDeArchivos("Prueba.txt", True)
    # 2. Escribir: Añade "Hola mundo\n" al final del archivo.
    escritor.escribir("Hola mundo\n")
    # 3. Cerrar: Cierra el archivo, asegurando que los datos se guarden.
    escritor.cerrar()


if __name__ == "__main__":
    main()