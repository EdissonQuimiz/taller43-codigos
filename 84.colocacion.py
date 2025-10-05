import random # Importa el módulo 'random' para colocar las minas de forma aleatoria.

# Define la clase principal del juego.
class Buscaminas:

    # Constructor de la clase. Se llama al crear un objeto (ej: Buscaminas(5, 6)).
    # Inicializa los tableros con el número de filas (f) y columnas (c) dadas.
    def __init__(self, f, c):
        # Inicializa una lista (tablero real, donde -1 es mina) con 'f' elementos None.
        self.tablero = [None] * f
        # Inicializa el tablero que ve el usuario (con '_' para celdas no reveladas).
        self.tablero_usuario = [None] * f

        # Bucle para inicializar cada fila de ambos tableros.
        for i in range(f):
            # Inicializa la fila del tablero real con ceros (0).
            self.tablero[i] = [0] * c
            # Inicializa la fila del tablero del usuario con guiones bajos ('_').
            self.tablero_usuario[i] = ['_'] * c

    # ---

    # Método para colocar una cantidad específica de minas (-1) en el tablero real de forma aleatoria.
    def colocar_minas(self, minas):
        while(minas > 0):
            # Genera coordenadas aleatorias para la fila y la columna.
            fila = random.randint(0, len(self.tablero) - 1)
            columna = random.randint(0, len(self.tablero[fila]) - 1)
            
            # Comprueba que la celda aún no contenga una mina (valor 0).
            if (self.tablero[fila][columna] == 0):
                self.tablero[fila][columna] = -1 # Coloca la mina.
                minas -= 1 # Decrementa el contador de minas restantes.

    # ---
    
    # Método para calcular y colocar los números (conteo de minas adyacentes) en el tablero real.
    def colocar_numeros(self):
        # Listas de offsets (desplazamientos) para revisar las 8 celdas vecinas.
        filas = [0, 0, -1, 1, 1, 1, -1, -1]
        cols =  [1, -1, 0, 0, 1, -1, 1, -1]

        # Recorre cada celda del tablero.
        for f in range(len(self.tablero)):
            for c in range(len(self.tablero[f])):
                # Solo opera si la celda actual es una mina (-1).
                if(self.tablero[f][c] == -1):
                    contador = 0
                    # Itera sobre las 8 direcciones vecinas.
                    while(contador < 8):
                        nueva_fila = f + filas[contador]
                        nueva_columna = c + cols[contador]
                        
                        # Comprueba que la celda vecina esté dentro de los límites del tablero
                        # y que NO sea otra mina (-1).
                        if (nueva_fila >= 0 and nueva_fila < len(self.tablero) and
                            nueva_columna >= 0 and nueva_columna < len(self.tablero[nueva_fila]) and
                            self.tablero[nueva_fila][nueva_columna] != -1):

                            # Incrementa el número de la celda vecina.
                            self.tablero[nueva_fila][nueva_columna] += 1

                        contador += 1

    # ---
    
    # Método para "jugar" o revelar una pieza en la posición (f, c).
    # Utiliza recursividad para revelar celdas vacías adyacentes (comportamiento de "cascada").
    def colocar_pieza(self, f, c, pierde = True):
        # Offsets para revisar celdas vecinas (igual que en colocar_numeros).
        filas = [0, 0, -1, 1, 1, 1, -1, -1]
        cols =  [1, -1, 0, 0, 1, -1, 1, -1]

        # Comprueba que las coordenadas (f, c) estén dentro de los límites.
        if (f >= 0 and f < len(self.tablero) and
            c >= 0 and c < len(self.tablero[f])):

            # 1. CASO RECURSIVO (Celda vacía: 0)
            # Si la celda no ha sido revelada ('_') y no tiene minas adyacentes (0).
            if(self.tablero_usuario[f][c] == '_' and self.tablero[f][c] == 0):
                self.tablero_usuario[f][c] = str(self.tablero[f][c]) # Revela la celda como '0'.
                contador = 0
                # Llama recursivamente a 'colocar_pieza' para las 8 celdas vecinas.
                while(contador < 8):
                    nueva_fila = f + filas[contador]
                    nueva_columna = c + cols[contador]
                    # La variable 'pierde' se usa para manejar la condición de victoria/derrota, 
                    # pero aquí se pasa 'False' para evitar un juego inmediato al hacer la cascada.
                    pierde = self.colocar_pieza(nueva_fila, nueva_columna, False)
                    contador += 1
                    
            # 2. CASO LÍMITE (Celda con número: > 0)
            # Si la celda tiene minas adyacentes (es un número).
            elif(self.tablero[f][c] > 0):
                self.tablero_usuario[f][c] = str(self.tablero[f][c]) # Revela el número.
                pierde = False # El juego continúa.
            
            # 3. CASO DE MINA O YA REVELADA (Celda con mina: -1)
            # Si se revela una mina, o si la celda ya estaba revelada.
            else:
                self.tablero_usuario[f][c] = str(self.tablero[f][c]) # Revela el contenido (Mina o 0).
        
        # Devuelve el estado de la partida: True si el jugador perdió (al inicio) o False si sigue jugando.
        return pierde

    # ---
    
    # Método especial que define cómo se debe representar el objeto como cadena (ej: cuando se usa print()).
    def __str__ (self):
        contenido = ""
        
        # 1. Muestra el Tablero Real (con minas 'M' y números/ceros).
        for f in range(len(self.tablero)):
            for c in range(len(self.tablero[f])):
                if(self.tablero[f][c] == -1):
                    contenido += ("M\t") # Representa la mina como 'M'.
                else:
                    contenido += str(self.tablero[f][c]) + "\t" # Muestra el número.
            contenido += "\n" # Salto de línea para la siguiente fila.

        contenido += " - - Tablero Usuario \n"

        # 2. Muestra el Tablero del Usuario (lo que ve el jugador).
        for f in range(len(self.tablero_usuario)):
            for c in range(len(self.tablero_usuario[f])):
                contenido += str(self.tablero_usuario[f][c]) + "\t"
            contenido += "\n"

        return contenido
    

# ---
# Bloque de ejecución principal.
if __name__ == "__main__":
    # 1. Inicializa el juego con un tablero de 5x6.
    buscaminas = Buscaminas(5, 6)
    print("1. Tableros Iniciales (5x6 con ceros y guiones bajos):")
    print(buscaminas)
    
    # 2. Coloca 3 minas aleatoriamente.
    buscaminas.colocar_minas(3)
    print("2. Tablero con 3 Minas (-1):")
    print(buscaminas)
    
    # 3. Calcula y coloca los números de adyacencia.
    buscaminas.colocar_numeros()
    print("3. Tablero con Números y Minas:")
    print(buscaminas)
    
    # 4. Simula la revelación de una pieza en (0, 0).
    # Si esta celda es 0, se activará la "cascada" recursiva.
    buscaminas.colocar_pieza(0, 0)
    print("4. Tablero del Usuario Después de Revelar (0, 0):")
    print(buscaminas)