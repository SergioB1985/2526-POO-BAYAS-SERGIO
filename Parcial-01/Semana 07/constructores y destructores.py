class Usuario: # Clase que representa un usuario del sistema
    def __init__(self, nombre, edad): # Constructor __init__, se ejecuta al crear el objeto
        self.nombre = nombre
        self.edad = edad
        print(f"Usuario creado: {self.nombre}, {self.edad} años.")

    def mostrar_datos(self): # Función para mostrar los datos del usuario
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def __del__(self): # Destructor __del__, que se ejecuata al eliminar el objeto, cuando se llama con 'del', o finaliza el programa
        print(f"El usuario '{self.nombre}' ha sido eliminado del sistema.")

def main(): # Función principal del programa
    # Ingreso de datos por teclado
    nombre = input("Ingrese el nombre del usuario: ")
    edad = int(input("Ingrese la edad del usuario: "))

    # Creación del objeto (llama al constructor)
    usuario = Usuario(nombre, edad)

    print("\nDatos del usuario registrado:")
    usuario.mostrar_datos()

    # Opción para eliminar el objeto
    opcion = input("\n¿Desea eliminar el usuario? (s/n): ").lower()

    if opcion == "s":
        del usuario  # Aquí se llama al destructor __del__
        print("Objeto eliminado correctamente.")

    else:
        print("El usuario permanece activo.")


if __name__ == "__main__":
    main()