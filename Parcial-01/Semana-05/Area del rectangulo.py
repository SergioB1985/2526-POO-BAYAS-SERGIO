class AreaRectangulo: # Clase para representar un rectangulo y calcular su área
    def __init__(self, nombre_figura, largo, ancho): # Constructor de la clase
        self.nombre_figura = nombre_figura # Variable de tipo string
        self.largo = largo                 # Variable de tipo float
        self.ancho = ancho                 # Variable de tipo float

    def calcular_area(self): # Metodo para calcular el área del rectangulo
        area = self.largo * self.ancho # Calcula el área
        return area # Retorna el área calculada

    def verificar_area_minima(self, area_minima): # Metodo para verificar si el área cumple con el valor minimo
        area_actual = self.calcular_area() # Obtiene el area actual
        cumple_minimo = area_actual >= area_minima # Verifica si el área es mayor o igual al minimo y retorna booleano
        return cumple_minimo # Retorna True si cumple, False si no

    def mostrar_resultados(self): # Metodo para mostrar los resultados del calculo
        area = self.calcular_area() # Calcula el área
        area_minima = 10 # Valor minimo del area de tipo int

        print(f"\nFigura: {self.nombre_figura}")
        print(f"Largo: {self.largo} m")
        print(f"Ancho: {self.ancho} m")
        print(f"Área: {area:.2f} m²")

        if self.verificar_area_minima(area_minima): # Muestra si el área cumple con el valor minimo
            print("El área cumple con el valor mínimo.")
        else:
            print("El área NO cumple con el valor mínimo.")

# Programa principal
def main():
    print("=== Cálculo del Área de un Rectángulo ===")

    nombre_figura = "Rectángulo" # Nombre de la figura
    largo = float(input("Ingrese el largo del rectángulo (m): "))
    ancho = float(input("Ingrese el ancho del rectángulo (m): "))

    rectangulo = AreaRectangulo(nombre_figura, largo, ancho) # Crear instancia de rectangulo
    rectangulo.mostrar_resultados() # Muestra los resultados del cálculo


if __name__ == "__main__": # Ejecuta el programa principal
    main() # Llama a la función main