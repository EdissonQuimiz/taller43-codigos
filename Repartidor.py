from Mazo import Mazo
from Jugador import Jugador

class Repartidor:

    def __init__(self, lista_jugadores):
        self.jugadores = lista_jugadores
        self.resultados = []
        self.mazo = Mazo()

    def repartir_cartas(self):
        for jugador in self.jugadores:
            cartas = [self.mazo.obtener_siguiente_carta(), self.mazo.obtener_siguiente_carta()]
            jugador.asignar_cartas(cartas)

    def jugar(self):
        ganador = 0
        valor = 0
        self.mazo.revolver()
        self.repartir_cartas()
        print('Juego iniciado hay:', len(self.jugadores))

        for i in range(len(self.jugadores)):
            suma = self.jugadores[i].jugar(self.mazo)
            resultado = 21 - suma
            if resultado > valor and resultado < 0:
                valor = resultado
                ganador = i
            print('La suma de', i, 'es', suma)
            self.resultados.append(resultado)

        print('Los resultados son', self.resultados, self.jugadores[ganador].nombre, str(valor))

j1 = Jugador('Jugador 1')
j2 = Jugador('Jugador 2')
repartidor = Repartidor([j1,j2])
repartidor.jugar()