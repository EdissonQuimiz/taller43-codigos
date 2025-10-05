class Recursividad:
    
    # Método para calcular el factorial de un número 'n' de forma recursiva.
    def calcular_factorial(self, n):
        # El factorial solo está definido para enteros no negativos.
        if n < 0:
            # Devuelve None para indicar un valor no válido.
            return None
        # El factorial de 0 y 1 es 1.
        if n == 0 or n == 1:
            return 1
            
        else:
            # El factorial de 'n' es 'n' multiplicado por el factorial de 'n-1'.
            return n * self.calcular_factorial(n - 1)
        
def main():
    # Crea una instancia (objeto) de la clase Recursividad.
    instancia_recursividad = Recursividad()
    
    # Llama al método calcular_factorial con el número 5.
    resultado = instancia_recursividad.calcular_factorial(5)
    
    # Imprime el resultado formateado, mostrando el cálculo: "El factorial de 5 es: 120"
    print(f"El factorial de 5 es: {resultado}")

if __name__ == "__main__":
    main()