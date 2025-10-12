
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


    def pedir_letra(self):
        letra = input("Digite una letra:")
        return self.quitar_acentos(letra.lower())


    def buscar_letra(self, letra):  
        veces = 0
        for i in range(len(self.palabra_secreta)):
            if (self.palabra_secreta[i] == letra):
                veces += 1
                self.palabra_usuario = self.palabra_usuario[:i] + letra + self.palabra_usuario[i+1:]

        return veces


    def determinar_si_gano(self):
        return self.palabra_usuario.find("?") == -1


    def jugar(self):
        while(not self.determinar_si_gano() and self.intentos > 0):
            self.imprimir_estado()
            letra = self.pedir_letra()
            veces = self.buscar_letra(letra)
            if(veces == 0):
                self.intentos -= 1

       
        if(self.intentos == 0):
            print("Perdió :(")
        else:
            print("Ganó :)")


def main():
    ahorcado = Ahorcado("pArAlElepipEdo")
    ahorcado.jugar()