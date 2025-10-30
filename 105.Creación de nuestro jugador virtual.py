from Interfaz import Interfaz
from Mazo import Mazo

class JugadorVirtual:

    def __init__(self, nombre, cartas = []):
        self.nombre = nombre
        self.cartas = cartas

    def asignar_cartas(self, cartas):
        self.cartas = cartas

    def imprimir(self):
        print(self.nombre, "estas son sus cartas")
        for carta in self.cartas:
            carta.imprimir()

        print("Suma: ", self.sumar_cartas())
    def sumar_cartas(self):
        suma = 0
        aces = 0
        for carta in self.cartas:
            valor = carta.obtener_numero()
            if valor == 1:
                aces += 1
                
            suma += valor

        if aces > 0 and suma + 10 <= 21:
            
            suma += 10

        return suma

def imprimir_juego(self):
    cartas = ['-']
    for i in range(1, len(self.cartas)):
        cartas.append(self.cartas[i].numero)

    print(cartas)

def jugar(self, mazo):
    if self.sumar_cartas() < 16:
        self.cartas.append(mazo.obtener_siguiente_carta())
        if self.sumar_cartas() < 16:
            self.imprimir_juego()
        return self.sumar_cartas()

if __name__ == "__main__":
    mazo = Mazo()
    jugador1 = Jugador("Juan")
    print(jugador1.jugar(mazo))
