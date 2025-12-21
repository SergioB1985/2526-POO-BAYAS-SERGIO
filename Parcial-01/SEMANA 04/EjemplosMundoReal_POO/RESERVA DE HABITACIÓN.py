# Ejemplo de un sistema de reservas de habitación de hotel utilizando POO
class Habitacion: # Clase base para habitaciones de hotel
    def __init__(self, numero, precio): # Constructor de la clase Habitación
        self.numero = numero
        self.precio = precio
        self.disponible = True

    def reservar(self): # Metodo para reservar la habitación
        if self.disponible: # Verificar si la habitación esta disponible
            self.disponible = False
            return "Habitación reservada con éxito."
        else:
            return "La habitación no está disponible."

    def liberar(self): # Metodo para liberar la habitación
        self.disponible = True

    def descripcion(self): # Metodo para describir la habitación
        return "Habitación estándar"


class HabitacionVIP(Habitacion): # Clase derivada para habitación VIP
    def __init__(self, numero, precio, servicios): # Constructor de la clase Habitación VIP
        super().__init__(numero, precio) # Llamada al constructor de la clase base
        self.servicios = servicios # Servicios adicionales para la habitación VIP

    def descripcion(self): # Metodo para describir la habitación VIP
        return f"Habitación VIP con servicios: {', '.join(self.servicios)}" # Descripción de la habitación VIP
def main(): # Función principal para interactuar con el usuario
    # Crear habitaciones disponibles
    habitaciones = { # Diccionario de habitaciones
        101: Habitacion(101, 50),
        201: HabitacionVIP(201, 120, ["Jacuzzi", "Vista al mar"])
    }

    print("=== Sistema de Reservas de Hotel ===")
    print("Habitaciones disponibles:")
    for h in habitaciones.values():
        print(f"Habitación {h.numero} - {h.descripcion()} - ${h.precio}")

    try:
        numero = int(input("\nIngrese el número de la habitación a reservar: "))

        if numero in habitaciones:
            habitacion = habitaciones[numero] # Obtener la habitación seleccionada
            print(habitacion.descripcion()) # Mostrar la descripción de la habitación
            print(habitacion.reservar()) # Intentar reservar la habitación
        else:
            print("La habitación ingresada no existe.")
    except ValueError:
        print("Error: debe ingresar un número de habitación válido.")


# Punto de entrada del programa
if __name__ == "__main__": # Llamada a la función principal
    main()