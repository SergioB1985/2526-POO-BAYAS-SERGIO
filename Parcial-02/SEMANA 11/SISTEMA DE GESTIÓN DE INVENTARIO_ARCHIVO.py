import json # Permite trabajar con archivos JSON para guardar y cargar el inventario
import os # Permite verificar la existencia de archivos y manejar rutas


# ==============================
# CLASE PRODUCTO
# ==============================

class Producto: # Clase que representa un producto en el inventario
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters que permiten acceder a los atributos privados del producto
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters que permiten modificar los atributos del producto, con validaciones para cantidad y precio
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio

    # Convertir objeto a diccionario (serialización) que facilita guardar en formato JSON
    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    # Crear objeto desde diccionario (deserialización) que facilita cargar desde formato JSON
    @staticmethod # Método estático que no depende de una instancia específica de la clase
    def from_dict(data): # Recibe un diccionario con los datos del producto y devuelve una instancia de Producto
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"]) # Crea un nuevo producto usando los datos del diccionario

    def __str__(self): # Método que define cómo se representa el producto como cadena de texto, útil para mostrar información del producto
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"


# ==============================
# CLASE INVENTARIO
# ==============================

class Inventario: # Clase que maneja el inventario de productos, permitiendo agregar, eliminar, actualizar y buscar productos
    def __init__(self): # Método constructor que inicializa el inventario con un diccionario vacío para almacenar los productos
        self.productos = {}  # Diccionario {id: Producto}

    # Metodo que permite añadir producto
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos: # Verifica si el ID del producto ya existe en el inventario para evitar duplicados
            print("❌ El ID ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("✅ Producto agregado correctamente.")

    # Metodo que permite eliminar producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos: # Permite verificar si el producto existe antes de intentar eliminarlo, evitando errores
            del self.productos[id_producto] # Elimina el producto del diccionario usando su ID como clave
            print("🗑 Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    # Metodo que permite actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos: # Permite verificar si el producto existe antes de intentar actualizarlo, evitando errores
            if cantidad is not None: # Permita verificar si se ha proporcionado una nueva cantidad antes de actualizarla, evitando cambios no deseados
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None: # Permite verificar si se ha proporcionado un nuevo precio antes de actualizarlo, evitando cambios no deseados
                self.productos[id_producto].set_precio(precio)
            print("🔄 Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    # Metodo que permite buscar por nombre
    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        return resultados

    # Metodo que permite mostrar todos los productos en el inventario, verificando primero si el inventario está vacío para informar al usuario
    def mostrar_todos(self):
        if not self.productos: # Verifica si el diccionario de productos está vacío, lo que indica que no hay productos en el inventario
            print("📦 Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    # Metodo que permite guardar en archivo
    def guardar_en_archivo(self, archivo="inventario.json"):
        data = {id: prod.to_dict() for id, prod in self.productos.items()} # Crea un nuevo diccionario donde cada clave es el ID del producto y el valor es el resultado de llamar al método to_dict() del producto, lo que facilita la conversión a formato JSON
        with open(archivo, "w") as f: # Abre el archivo en modo escritura, lo que permite guardar el inventario en un archivo JSON
            json.dump(data, f, indent=4) # Escribe el diccionario de productos en el archivo en formato JSON, con una indentación de 4 espacios para mejorar la legibilidad del archivo
        print("💾 Inventario guardado correctamente.")

    # Metodo que permite cargar desde archivo
    def cargar_desde_archivo(self, archivo="inventario.json"):
        if os.path.exists(archivo): # Verifica si el archivo de inventario existe antes de intentar cargarlo, lo que evita errores al intentar abrir un archivo inexistente
            with open(archivo, "r") as f: # Abre el archivo en modo lectura, lo que permite cargar el inventario desde un archivo JSON
                data = json.load(f) # Lee el contenido del archivo y lo convierte de formato JSON a un diccionario de Python, lo que facilita la manipulación de los datos del inventario
                for id, prod_data in data.items(): # Itera sobre cada par clave-valor en el diccionario de datos, donde la clave es el ID del producto y el valor es otro diccionario con los datos del producto
                    self.productos[id] = Producto.from_dict(prod_data)
            print("📂 Inventario cargado correctamente.")
        else:
            print("⚠ No existe archivo previo de inventario.")


# ==============================
# MENÚ INTERACTIVO
# ==============================

def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("❌ No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo()

        elif opcion == "7":
            inventario.guardar_en_archivo()
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida.")


# Ejecuta el programa
if __name__ == "__main__":
    menu()