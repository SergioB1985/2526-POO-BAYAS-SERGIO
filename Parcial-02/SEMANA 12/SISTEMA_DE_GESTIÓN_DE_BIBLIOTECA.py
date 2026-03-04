class Libro: # Clase para representar un libro
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla (inmutable)
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True # Estado del libro (disponible o prestado)

    def __str__(self): # Representación del libro para impresión
        estado = "Disponible" if self.disponible else "Prestado" # Mostrar estado del libro
        return f"Título: {self.info[0]} | Autor: {self.info[1]} | Categoría: {self.categoria} | ISBN: {self.isbn} | Estado: {estado}"


class Usuario: # Clase para representar un usuario
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista

    def prestar_libro(self, libro): # Agregar libro a la lista de prestados del usuario
        self.libros_prestados.append(libro) # Agregar libro a la lista de prestados del usuario

    def devolver_libro(self, libro): # Eliminar libro de la lista de prestados del usuario
        if libro in self.libros_prestados: # Verificar si el libro está en la lista de prestados del usuario
            self.libros_prestados.remove(libro) # Eliminar libro de la lista de prestados del usuario

    def listar_prestados(self): # Mostrar los libros prestados por el usuario
        if not self.libros_prestados: # Verificar si el usuario no tiene libros prestados
            print("No tiene libros prestados.")
        else:
            for libro in self.libros_prestados: # Mostrar cada libro prestado por el usuario
                print(libro)


class Biblioteca: # Clase principal para gestionar la biblioteca
    def __init__(self): # Inicializar la biblioteca con diccionarios para libros y usuarios, y un conjunto para IDs únicos
        self.libros = {}  # Diccionario ISBN: Libro
        self.usuarios = {}  # Diccionario ID: Usuario
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    # ================== LIBROS ==================
    def añadir_libro(self): # Agregar un nuevo libro a la biblioteca
        isbn = input("ISBN: ") # Solicitar ISBN del libro
        if isbn in self.libros: # Verificar si el ISBN ya existe en la biblioteca
            print("⚠ El libro ya existe.")
            return
        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("Categoría: ")
        self.libros[isbn] = Libro(titulo, autor, categoria, isbn)
        print("✅ Libro añadido correctamente.")

    def quitar_libro(self): # Eliminar un libro de la biblioteca
        isbn = input("ISBN del libro a eliminar: ") # Solicitar ISBN del libro a eliminar
        if isbn in self.libros: # Verificar si el ISBN existe en la biblioteca
            del self.libros[isbn] # Eliminar el libro del diccionario de libros
            print("✅ Libro eliminado.")
        else:
            print("⚠ Libro no encontrado.")

    def mostrar_libros(self): # Mostrar todos los libros registrados en la biblioteca
        if not self.libros: # Verificar si no hay libros registrados en la biblioteca
            print("No hay libros registrados.")
        else:
            for libro in self.libros.values():
                print(libro)

    # ================== USUARIOS ==================
    def registrar_usuario(self): # Registrar un nuevo usuario en la biblioteca
        user_id = input("ID de usuario: ") # Solicitar ID del usuario
        if user_id in self.ids_usuarios: # Verificar si el ID ya está registrado en la biblioteca
            print("⚠ ID ya registrado.")
            return
        nombre = input("Nombre del usuario: ")
        self.usuarios[user_id] = Usuario(nombre, user_id)
        self.ids_usuarios.add(user_id)
        print("✅ Usuario registrado.")

    def eliminar_usuario(self): # Eliminar un usuario registrado en la biblioteca
        user_id = input("ID del usuario a eliminar: ") # Solicitar ID del usuario a eliminar
        if user_id in self.ids_usuarios: # Verificar si el ID existe en la biblioteca
            del self.usuarios[user_id] # Eliminar el usuario del diccionario de usuarios
            self.ids_usuarios.remove(user_id)
            print("✅ Usuario eliminado.")
        else:
            print("⚠ Usuario no encontrado.")

    def mostrar_usuarios(self): # Mostrar todos los usuarios registrados en la biblioteca
        if not self.usuarios: # Verificar si no hay usuarios registrados en la biblioteca
            print("No hay usuarios registrados.")
        else:
            for usuario in self.usuarios.values(): # Mostrar cada usuario registrado en la biblioteca
                print(f"Nombre: {usuario.nombre} | ID: {usuario.user_id}")

    # ================== PRÉSTAMOS ==================
    def prestar_libro(self): # Realizar el préstamo de un libro a un usuario
        isbn = input("ISBN del libro: ") # Solicitar ISBN del libro a prestar
        user_id = input("ID del usuario: ") # Solicitar ID del usuario que va a recibir el libro

        if isbn not in self.libros: # Verificar si el ISBN no existe en la biblioteca
            print("⚠ Libro no encontrado.")
            return
        if user_id not in self.ids_usuarios: # Verificar si el ID del usuario no existe en la biblioteca
            print("⚠ Usuario no encontrado.")
            return

        libro = self.libros[isbn] # Obtener el libro del diccionario de libros utilizando el ISBN
        usuario = self.usuarios[user_id] # Obtener el usuario del diccionario de usuarios utilizando el ID del usuario

        if libro.disponible: # Verificar si el libro está disponible para préstamo
            libro.disponible = False
            usuario.prestar_libro(libro)
            print("✅ Préstamo realizado.")
        else:
            print("⚠ Libro no disponible.")

    def devolver_libro(self): # Realizar la devolución de un libro por parte de un usuario
        isbn = input("ISBN del libro: ")
        user_id = input("ID del usuario: ")

        if isbn in self.libros and user_id in self.ids_usuarios: # Verificar si el ISBN y el ID del usuario existen en la biblioteca
            libro = self.libros[isbn]
            usuario = self.usuarios[user_id]

            if libro in usuario.libros_prestados: # Verificar si el libro está en la lista de prestados del usuario
                libro.disponible = True
                usuario.devolver_libro(libro)
                print("✅ Libro devuelto.")
            else:
                print("⚠ El usuario no tiene ese libro.")
        else:
            print("⚠ Datos incorrectos.")

    def listar_prestados_usuario(self): # Listar los libros prestados por un usuario específico
        user_id = input("ID del usuario: ")
        if user_id in self.ids_usuarios: # Verificar si el ID del usuario existe en la biblioteca
            self.usuarios[user_id].listar_prestados()
        else:
            print("⚠ Usuario no encontrado.")


# ================== MENÚS ==================

def submenu_libros(biblioteca): # Submenú para gestionar libros en la biblioteca
    while True:
        print("\n--- SUBMENÚ LIBROS ---")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Mostrar libros")
        print("4. Volver")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            biblioteca.añadir_libro()
        elif opcion == "2":
            biblioteca.quitar_libro()
        elif opcion == "3":
            biblioteca.mostrar_libros()
        elif opcion == "4":
            break
        else:
            print("⚠ Opción inválida.")


def submenu_usuarios(biblioteca): # Submenú para gestionar usuarios en la biblioteca
    while True:
        print("\n--- SUBMENÚ USUARIOS ---")
        print("1. Registrar usuario")
        print("2. Eliminar usuario")
        print("3. Mostrar usuarios")
        print("4. Volver")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            biblioteca.registrar_usuario()
        elif opcion == "2":
            biblioteca.eliminar_usuario()
        elif opcion == "3":
            biblioteca.mostrar_usuarios()
        elif opcion == "4":
            break
        else:
            print("⚠ Opción inválida.")


def submenu_prestamos(biblioteca): # Submenú para gestionar préstamos de libros en la biblioteca
    while True:
        print("\n--- SUBMENÚ PRÉSTAMOS ---")
        print("1. Prestar libro")
        print("2. Devolver libro")
        print("3. Listar libros prestados por usuario")
        print("4. Volver")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            biblioteca.prestar_libro()
        elif opcion == "2":
            biblioteca.devolver_libro()
        elif opcion == "3":
            biblioteca.listar_prestados_usuario()
        elif opcion == "4":
            break
        else:
            print("⚠ Opción inválida.")


def menu_principal(): # Menú principal para gestionar la biblioteca digital
    biblioteca = Biblioteca()

    while True:
        print("\n===== SISTEMA BIBLIOTECA DIGITAL =====")
        print("1. Gestión de Libros")
        print("2. Gestión de Usuarios")
        print("3. Gestión de Préstamos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            submenu_libros(biblioteca)
        elif opcion == "2":
            submenu_usuarios(biblioteca)
        elif opcion == "3":
            submenu_prestamos(biblioteca)
        elif opcion == "4":
            print("👋 Cerrando sistema...")
            break
        else:
            print("⚠ Opción inválida.")


# Ejecutar sistema
menu_principal()
