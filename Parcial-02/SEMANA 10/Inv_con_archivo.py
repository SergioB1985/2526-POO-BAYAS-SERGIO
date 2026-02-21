import os # Permite trabajar con archivos y directorios

class Producto: # Clase para presentar cada producto del inventario
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters que permite acceder a los atributos privados de la clase Producto
    def get_id(self): # Permite acceder al ID del producto
        return self.__id

    def get_nombre(self): # Permite acceder al nombre del producto
        return self.__nombre

    def get_cantidad(self): # Permite acceder a la cantidad del producto
        return self.__cantidad

    def get_precio(self): # Permite acceder al precio del producto
        return self.__precio

    # Setters que permite modificar los atributos privados a la clase Producto
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self): # Permite convertir el objeto Producto a una cadena de texto para guardarlo en el archivo
        return f"{self.__id},{self.__nombre},{self.__cantidad},{self.__precio}"

    # Método para mostrar bonito en pantalla
    def mostrar(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"


class Inventario: # Clase para manejar el inventario de productos, incluyendo la carga y guardado en archivo
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo # Nombre del archivo donde se guardará el inventario
        self.cargar_desde_archivo() # Carga el inventario desde el archivo al iniciar el programa

    # ===============================
    # CARGAR INVENTARIO DESDE ARCHIVO
    # ===============================
    def cargar_desde_archivo(self): # Método para cargar el inventario desde un archivo de texto. Si el archivo no existe, se crea automáticamente.
        try:
            if not os.path.exists(self.archivo): # Verifica si el archivo existe, si no, lo crea automáticamente
                open(self.archivo, "w").close() # Crea un archivo vacío
                print("📁 Archivo inventario.txt creado automáticamente.") # Si el archivo no existe, se crea automáticamente y se muestra un mensaje informativo.                 return

            with open(self.archivo, "r") as file: # Abre el archivo en modo lectura para cargar los productos al inventario
                for linea in file: # Lee cada línea del archivo, la limpia de espacios y la divide por comas para extraer los datos del producto
                    datos = linea.strip().split(",") # Se espera que cada línea tenga el formato: ID,Nombre,Cantidad,Precio
                    if len(datos) == 4: # Verifica que la línea tenga el formato correcto antes de intentar crear un producto
                        id_p = int(datos[0])
                        nombre = datos[1]
                        cantidad = int(datos[2])
                        precio = float(datos[3])
                        self.productos.append(Producto(id_p, nombre, cantidad, precio))

            print("📂 Inventario cargado correctamente desde archivo.")

        except FileNotFoundError: # Si el archivo no se encuentra, se muestra un mensaje de error. Sin embargo, con la verificación previa, este error no debería ocurrir.
            print("❌ Error: Archivo no encontrado.")
        except PermissionError: # Si no se tienen permisos para acceder al archivo, se muestra un mensaje de error.
            print("❌ Error: No tiene permisos para acceder al archivo.")
        except ValueError:
            print("❌ Error: Datos corruptos en el archivo.")

    # ===============================
    # GUARDAR INVENTARIO EN ARCHIVO
    # ===============================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as file: # Abre el archivo en modo escritura para guardar el inventario actualizado. Esto sobrescribe el contenido anterior.
                for producto in self.productos: # Escribe cada producto en una nueva línea del archivo utilizando el método __str__ de la clase Producto para formatear los datos correctamente.
                    file.write(str(producto) + "\n") # Cada producto se guarda en una nueva línea con el formato: ID,Nombre,Cantidad,Precio
            print("💾 Cambios guardados correctamente en el archivo.")
        except PermissionError: # Si no se tienen permisos para escribir en el archivo, se muestra un mensaje de error.
            print("❌ Error: No tiene permisos para escribir en el archivo.")

    # ===============================
    # MÉTODOS DEL INVENTARIO
    # ===============================

    def agregar_producto(self, producto): # Método para agregar un nuevo producto al inventario. Verifica que el ID del producto no exista antes de agregarlo.
        for p in self.productos: # Verifica que el ID del producto no exista antes de agregarlo. Si el ID ya existe, se muestra un mensaje de error y no se agrega el producto.
            if p.get_id() == producto.get_id(): # Si el ID del producto ya existe en el inventario, se muestra un mensaje de error y no se agrega el producto.
                print("❌ Error: El ID ya existe.")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("✅ Producto agregado correctamente y guardado en archivo.")

    def eliminar_producto(self, id_producto): # Método para eliminar un producto del inventario por su ID. Busca el producto por ID, lo elimina de la lista y guarda los cambios en el archivo.
        for p in self.productos: # Busca el producto por ID, lo elimina de la lista y guarda los cambios en el archivo. Si el producto no se encuentra, se muestra un mensaje de error.
            if p.get_id() == id_producto: # Si se encuentra el producto con el ID especificado, se elimina de la lista de productos y se guardan los cambios en el archivo.
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("✅ Producto eliminado y cambios guardados.")
                return

        print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None): # Método para actualizar la cantidad y/o precio de un producto por su ID. Busca el producto por ID, actualiza los campos especificados y guarda los cambios en el archivo.
        for p in self.productos: # Permite actualizar la cantidad y/o precio de un producto por su ID. Busca el producto por ID, actualiza los campos especificados y guarda los cambios en el archivo. Si el producto no se encuentra, se muestra un mensaje de error.
            if p.get_id() == id_producto: # Si se encuentra el producto con el ID especificado, se actualizan los campos de cantidad y precio según los valores proporcionados (si no son None) y se guardan los cambios en el archivo.
                if nueva_cantidad is not None: # Si se proporciona una nueva cantidad, se actualiza la cantidad del producto utilizando el setter correspondiente.
                    p.set_cantidad(nueva_cantidad) # Si se proporciona un nuevo precio, se actualiza el precio del producto utilizando el setter correspondiente.
                if nuevo_precio is not None: # Si se proporciona un nuevo precio, se actualiza el precio del producto utilizando el setter correspondiente.
                    p.set_precio(nuevo_precio)

                self.guardar_en_archivo()
                print("✅ Producto actualizado y guardado en archivo.")
                return

        print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre): # Método para buscar productos por nombre. Devuelve una lista de productos cuyo nombre contiene la cadena de búsqueda (ignorando mayúsculas/minúsculas).
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_productos(self): # Método para mostrar todos los productos del inventario. Si el inventario está vacío, se muestra un mensaje informativo. De lo contrario, se muestra la lista de productos con su información formateada.
        if not self.productos:
            print("📦 Inventario vacío.")
        else:
            print("\n📋 LISTA DE PRODUCTOS:")
            for p in self.productos:
                print(p.mostrar())


# ===============================
# MENÚ PRINCIPAL
# ===============================
def menu():
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

        try:
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
                        print(p.mostrar())
                else:
                    print("❌ No se encontraron productos.")

            elif opcion == "5":
                inventario.mostrar_productos()

            elif opcion == "6":
                print("👋 Saliendo del sistema...")
                break

            else:
                print("❌ Opción inválida.")

        except ValueError:
            print("❌ Error: Ingrese valores numéricos válidos.")


if __name__ == "__main__":
    menu()