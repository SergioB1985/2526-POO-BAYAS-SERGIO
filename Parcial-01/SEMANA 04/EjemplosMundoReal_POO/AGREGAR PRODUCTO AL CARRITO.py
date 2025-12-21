# Sistema de Pedidos con POO: Agregar Productos al Carrito
class Producto: # Clse que representa un producto en el sistema de pedidos
    def __init__(self, nombre, precio): # Contructor de la clase Producto
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self): # Metodo para mostrar la información del producto
        return f"{self.nombre} - ${self.precio}"


class Carrito: # clase que representa el carrito de compras
    def __init__(self): # Constructor de la clase Carrito
        self.productos = []

    def agregar_producto(self, producto): # Metodo para agregar un producto al carrito
        self.productos.append(producto)

    def calcular_total(self): # Metodo para calcular el total del carrito
        return sum(producto.precio for producto in self.productos)

    def mostrar_carrito(self): # Metodo para mostrar los productos en el carrito
        for producto in self.productos:
            print(producto.mostrar_info())
        print(f"Total a pagar: ${self.calcular_total()}")


# Uso del sistema
def main(): # Función principal para interactuar con el usuario
    carrito = Carrito()

    print("=== Sistema de Pedidos ===")

    while True: # Bucle para agregar productos al carrito, siempre y cuando el usuario no decida salir
        nombre = input("\nIngrese el nombre del producto (o 'salir' para finalizar): ")
        if nombre.lower() == "salir":
            break

        try:
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(nombre, precio) # Crear una instancia de Producto
            carrito.agregar_producto(producto) # Agregar el producto al carrito
            print("Producto agregado al carrito.")
        except ValueError:
            print("Error: el precio debe ser un número válido.")
    print("=== Resumen del Carrito===")
    carrito.mostrar_carrito()


# Punto de entrada del programa
if __name__ == "__main__": # Llamada a la función principal
    main()