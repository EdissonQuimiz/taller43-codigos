class Ahorcado:

    def __init__(self, palabra="", intentos = 5):
        self.palabra_secreta = palabra
        self.palabra_usuario = "?" * len(palabra)
        self.intentos = intentos

    def imprimir_estado(self):
        print(self.palabra_usuario)
        print(self.palabra_secreta)
        print("Le quedan", self.intentos, "intentos")

    def quitar_acentos(self, palabra):
        acento = ["á", "é", "í", "ó", "ú", "ü"]
        reemplazos = ["a", "e", "i", "o", "u", "u"]
        for i in range(len(acento)):
            palabra = palabra.replace(acento[i], reemplazos[i])
        return palabra


def main():
    ahorcado = Ahorcado("paralelepípedo")
    ahorcado.imprimir_estado()
    print(ahorcado.quitar_acentos("paralelepípedo"))

if __name__ == "__main__":
    main()