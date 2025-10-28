from Mazo import Mazo
from Jugador import Jugador

class Repartidor:

    def __init__(self, lista_jugadores):
        self.lista_jugadores = lista_jugadores
        self.resultado = []
        self.mazo = Mazo()

    def repartir_cartas(self):
        for jugador in self.lista_jugadores:
            cartas = [self.mazo.obtener_siguiente_carta(), self.mazo.obtener_siguiente_carta()]
            jugador.asignar_cartas(cartas)

    def jugar(self):
        ganador = 0
        valor = 0
        self.mazo.revolver()
        self.repartir_cartas()

        for i in range(len(self.lista_jugadores)):
            suma = self.lista_jugadores[i].jugar(self.mazo)
            resultado = 21 - suma
            if resultado > valor and resultado < 0:
                valor = resultado
                ganador = i

            self.resultado.append(resultado)