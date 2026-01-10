class EstadoEstudiante: # Clase para menejar la información de un estudiante
    def __init__(self, nombre_estudiante, edad_estudiante): # Constructor de la clase
        self.nombre_estudiante = nombre_estudiante # Variable de tipo string
        self.edad_estudiante = edad_estudiante     # Variable de tipo int
        self.calificaciones = []                   # Lista para almacenar calificaciones de tipo float

    def agregar_calificacion(self, nota): # Metodo para agregar una calificación a la lista
        self.calificaciones.append(nota) # Agregar la calificación a la lista

    def calcular_promedio(self): # Metodo para calcular el promedio de las calificaciones
        if len(self.calificaciones) == 0: # Evita división para cero
            return 0.0 # Retorna 0 si no hay calificaciones
        promedio = sum(self.calificaciones) / len(self.calificaciones) # Calcula el promedio
        return promedio

    def verificar_aprobacion(self, promedio_minimo): # Metodo para verificar si el estudiante aprueba
        promedio_actual = self.calcular_promedio() # Obtiene el promedio actual
        aprueba = promedio_actual >= promedio_minimo # Verifica si el promedio es mayor o igual al minimo y retorna booleano
        return aprueba # Retorna True si aprueba, False si no

    def mostrar_informacion(self): # Metodo para mostrar la información del estudiante
        promedio = self.calcular_promedio() # Calcula el promedio
        estado_aprobacion = self.verificar_aprobacion(7.0) # Verifica si aprueba con promedio minimo de 7.0

        print("\n=== Información del Estudiante ===")
        print(f"Nombre: {self.nombre_estudiante}")
        print(f"Edad: {self.edad_estudiante} años")
        print(f"Promedio: {promedio:.2f}")

        if estado_aprobacion: # Muestra el estado de aprobación del estudiante
            print("Estado: APROBADO")
        else:
            print("Estado: REPROBADO")


# Programa principal
def main():
    print("=== Registro de Estudiante ===")

    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))

    estudiante = EstadoEstudiante(nombre, edad) # Crear instancia de Estudiante

    cantidad_notas = int(input("Ingrese la cantidad de calificaciones: ")) # Solicitar cantidad de calificaciones

    for i in range(cantidad_notas): # Bucle para ingresar cada calificación
        nota = float(input(f"Ingrese la calificación {i + 1}: ")) # Ingreso de la calificación
        estudiante.agregar_calificacion(nota) # Agregar calificación al estudiante

    estudiante.mostrar_informacion() # Muestra la información del estudiante

if __name__ == "__main__": # Ejecuta el programa principal
    main() # Llama a la función main