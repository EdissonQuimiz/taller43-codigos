def calcular_sumatoria(numero):
    resultando = 0
    
    #  CASO RECURSIVO (Para números POSITIVOS):
    # Si el 'numero' es mayor que 0, se ejecuta la sumatoria recursiva.
    if(numero > 0):
        # Suma el número actual más la llamada recursiva a la función
        # con 'numero - 1' (acercándose al 0, que es el caso base/parada).
        resultando = numero + calcular_sumatoria(numero-1)
    # Si 'numero' es 0 o negativo, la condición 'if' es Falsa.
    # El código salta a 'return resultando', donde 'resultando' sigue siendo 0.
    
    # Devuelve el valor acumulado (0 si el número inicial fue negativo).
    return resultando
def main():
    
    # Llama a la función con -1.
    # Dado que -1 NO es > 0, la función devuelve el valor inicial de 'resultando', que es 0.
    print(calcular_sumatoria(-1)) # El programa imprime 0
if __name__ == "__main__":
    main()