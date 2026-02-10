class Producto: # Clase para representar un producto en el inventario
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters que permite acceder a los atributos privados de la clase Producto
    def get_id(self): # Devuelve el ID del producto
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters que permite modificar los atributos privados de la clase Producto
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"

class Inventario: # Clase para gestionar el imnventario de productos
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto): # Función para agregar un producto al inventario
        for p in self.productos:
            if p.get_id() == producto.get_id(): # Verifica si el ID del producto ya existe en el inventario
                print("❌ Error: El ID ya existe.")
                return
        self.productos.append(producto) # Agrega el producto al inventario
        print("✅ Producto agregado correctamente.")

    def eliminar_producto(self, id_producto): # Función para eliminar un producto del inventario por su ID
        for p in self.productos:
            if p.get_id() == id_producto: # Verifica si el ID del producto coincide con el ID proporcionado
                self.productos.remove(p)
                print("✅ Producto eliminado.")
                return
        print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None): # Función para acxtualizar la cantidad y/o el precio de un producto en el inventario
        for p in self.productos: # Recorre la lista de productos para encontrar el producto con el ID proporcionado
            if p.get_id() == id_producto: # Verifica si el ID del producto coincide con el ID proporcionado
                if nueva_cantidad is not None: # Si se proporciona una nueva cantidad, actualizada la cantidad del producto en el inventario se actualiza
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None: # Si se proporciona un nuevo precio, actualizada el precio del producto en el inventario se actualiza
                    p.set_precio(nuevo_precio)
                print("✅ Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre): # Función para buscar productos en el inventario por su nombre
        resultados = []
        for p in self.productos: # Recorre la lista de productos para encontrar productos cuyo nombre coincida con el nombre proporcionado
            if nombre.lower() in p.get_nombre().lower(): # Verifica si el nombre del producto contiene el nombre proporcionado (ignorando mayúsculas y minusculas)
                resultados.append(p)
        return resultados

    def mostrar_productos(self): # función para mostrar todos los productos en el inventario
        if not self.productos: # Verifica si la lista de producto está vacía, si es asi, muestra un mensaje indicando que el inventario esta vacio
            print("📦 Inventario vacío.")
        else:
            for p in self.productos:
                print(p)

def menu(): # Función para mostrar el menú de opciones al usuario y gestionar las interacciones con el inventario
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = int(input("ID: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_p, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_p = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = int(input("ID del producto a actualizar: "))
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(id_p, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("❌ No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida.")

if __name__ == "__main__": # Punto de entrada del programa, se llama a la función
    menu()