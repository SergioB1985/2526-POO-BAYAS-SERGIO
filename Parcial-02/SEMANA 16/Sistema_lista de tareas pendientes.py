import tkinter as tk # Biblioteca para crear interfaces gráficas de usuario (GUI) en Python
from tkinter import messagebox # Biblioteca para mostrar cuadros de diálogo de mensajes en la interfaz gráfica

class TodoApp: # Clase principal de la aplicación de lista de tareas
    def __init__(self, root): # Constructor de la clase, se ejecuta al crear una instancia de la clase TodoApp
        self.root = root #
        self.root.title("Gestor de Tareas") # Establece el título de la ventana principal de la aplicación

        # Lista de tareas (texto, estado)
        self.tasks = [] # Lista para almacenar las tareas, cada tarea es una tupla que contiene el texto de la tarea y su estado (completada o no)

        # ----------- INTERFAZ -----------
        self.frame = tk.Frame(root) # Crea un marco (frame) dentro de la ventana principal para organizar los widgets de la interfaz
        self.frame.pack(padx=10, pady=10) # Agrega el marco a la ventana principal con un margen de 10 píxeles en los bordes

        # Campo de entrada
        self.entry = tk.Entry(self.frame, width=40) # Crea un campo de entrada (Entry) dentro del marco para que el usuario pueda escribir el texto de la tarea, con un ancho de 40 caracteres
        self.entry.grid(row=0, column=0, padx=5, pady=5) # Coloca el campo de entrada en la primera fila y primera columna del marco, con un margen de 5 píxeles en los bordes
        self.entry.focus() # Establece el foco en el campo de entrada para que el usuario pueda comenzar a escribir inmediatamente al abrir la aplicación

        # Botón agregar
        self.add_btn = tk.Button(self.frame, text="Agregar", command=self.add_task) # Crea un botón (Button) dentro del marco con el texto "Agregar" y asigna la función self.add_task como comando que se ejecutará cuando se haga clic en el botón
        self.add_btn.grid(row=0, column=1, padx=5) # Coloca el botón en la primera fila y segunda columna del marco, con un margen de 5 píxeles en el borde derecho

        # Lista de tareas
        self.listbox = tk.Listbox(self.frame, width=50, height=10) # Crea una lista (Listbox) dentro del marco para mostrar las tareas, con un ancho de 50 caracteres y una altura de 10 líneas
        self.listbox.grid(row=1, column=0, columnspan=2, pady=10) # Coloca la lista en la segunda fila y abarca ambas columnas del marco, con un margen de 10 píxeles en el borde inferior

        # Botón completar
        self.complete_btn = tk.Button(self.frame, text="Completar", command=self.complete_task) # Crea un botón dentro del marco con el texto "Completar" y asigna la función self.complete_task como comando que se ejecutará cuando se haga clic en el botón
        self.complete_btn.grid(row=2, column=0, pady=5) # Coloca el botón en la tercera fila y primera columna del marco, con un margen de 5 píxeles en el borde inferior

        # Botón eliminar
        self.delete_btn = tk.Button(self.frame, text="Eliminar", command=self.delete_task) # Crea un botón dentro del marco con el texto "Eliminar" y asigna la función self.delete_task como comando que se ejecutará cuando se haga clic en el botón
        self.delete_btn.grid(row=2, column=1, pady=5) # Coloca el botón en la tercera fila y segunda columna del marco, con un margen de 5 píxeles en el borde inferior

        # ----------- ATAJOS DE TECLADO -----------
        self.root.bind('<Return>', lambda event: self.add_task()) # Asocia la tecla "Enter" con la función self.add_task para que se ejecute cuando el usuario presione "Enter"
        self.root.bind('<c>', lambda event: self.complete_task()) # Asocia la tecla "c" con la función self.complete_task para que se ejecute cuando el usuario presione "c"
        self.root.bind('<C>', lambda event: self.complete_task()) # Asocia la tecla "C" (mayúscula) con la función self.complete_task para que se ejecute cuando el usuario presione "C"
        self.root.bind('<Delete>', lambda event: self.delete_task()) # Asocia la tecla "Delete" con la función self.delete_task para que se ejecute cuando el usuario presione "Delete"
        self.root.bind('<d>', lambda event: self.delete_task()) # Asocia la tecla "d" con la función self.delete_task para que se ejecute cuando el usuario presione "d"
        self.root.bind('<Escape>', lambda event: self.root.quit()) # Asocia la tecla "Escape" con la función self.root.quit para que se ejecute cuando el usuario presione "Escape", lo que cerrará la aplicación

    # ----------- FUNCIONES -----------
    def add_task(self): # Función para agregar una tarea a la lista
        task_text = self.entry.get().strip() # Obtiene el texto ingresado en el campo de entrada, elimina los espacios en blanco al principio y al final, y lo almacena en la variable task_text
        if task_text == "": # Si el texto de la tarea está vacío, muestra una advertencia al usuario y no agrega la tarea a la lista
            messagebox.showwarning("Advertencia", "Ingrese una tarea") # Muestra un cuadro de diálogo de advertencia con el título "Advertencia" y el mensaje "Ingrese una tarea"
            return

        self.tasks.append((task_text, False)) # Agrega una nueva tarea a la lista de tareas, representada como una tupla que contiene el texto de la tarea y un valor booleano que indica que la tarea no está completada (False)
        self.update_list() # Llama a la función self.update_list para actualizar la visualización de la lista de tareas en la interfaz gráfica
        self.entry.delete(0, tk.END) # Limpia el campo de entrada después de agregar la tarea, eliminando el texto ingresado para que el usuario pueda ingresar una nueva tarea

    def complete_task(self): # Función para marcar una tarea como completada
        try: # Intenta obtener el índice de la tarea seleccionada en la lista
            index = self.listbox.curselection()[0] # Obtiene el indice de la tarea seleccionada en la lista
            task_text, status = self.tasks[index] # Obtiene el texto y el estado de la tarea seleccionada utilizando el índice obtenido
            self.tasks[index] = (task_text, True) # Actualiza la tarea en la lista de tareas, marcándola como completada (True) mientras mantiene el mismo texto de la tarea
            self.update_list() # Llama a la función self.update_list para actualizar la visualización de la lista de tareas en la interfaz gráfica, reflejando el cambio de estado de la tarea seleccionada
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea")

    def delete_task(self): # Función para eliminar una tarea de la lista
        try:
            index = self.listbox.curselection()[0] # Obtiene el índice de la tarea seleccionada en la lista
            self.tasks.pop(index) # Elimina la tarea de la lista de tareas utilizando el índice obtenido
            self.update_list() # Llama a la función self.update_list para actualizar la visualización de la lista de tareas en la interfaz gráfica, reflejando la eliminación de la tarea seleccionada
        except IndexError: # Si no se ha seleccionado ninguna tarea, muestra una advertencia al usuario
            messagebox.showwarning("Advertencia", "Seleccione una tarea") # Muestra un cuadro de diálogo de advertencia con el título "Advertencia" y el mensaje "Seleccione una tarea"

    def update_list(self): # Función para actualizar la visualización de la lista de tareas en la interfaz gráfica
        self.listbox.delete(0, tk.END) # Elimina todos los elementos de la lista de tareas en la interfaz gráfica para prepararla para la actualización con las tareas actuales
        for task, status in self.tasks: # Itera sobre cada tarea en la lista de tareas, obteniendo el texto de la tarea y su estado (completada o no)
            if status: # Si la tarea está marcada como completada (True), se muestra con un símbolo de verificación (✔) y en color gris
                self.listbox.insert(tk.END, f"✔ {task}") # Inserta la tarea en la lista de tareas en la interfaz gráfica, precedida por un símbolo de verificación (✔) para indicar que está completada
                self.listbox.itemconfig(tk.END, fg="gray") # Configura el color del texto de la tarea recién insertada en la lista de tareas en la interfaz gráfica a gris para indicar que está completada
            else:
                self.listbox.insert(tk.END, f"✗ {task}") # Inserta la tarea en la lista de tareas en la interfaz gráfica, precedida por un símbolo de cruz (✗) para indicar que no está completada
                self.listbox.itemconfig(tk.END, fg="black") # Configura el color del texto de la tarea recién insertada en la lista de tareas en la interfaz gráfica


# ----------- EJECUCIÓN -----------
if __name__ == "__main__": # Verifica si el script se está ejecutando directamente (en lugar de ser importado como un módulo) y, si es así, ejecuta el bloque de código dentro de esta condición
    root = tk.Tk() # Crea una instancia de la clase Tk, que representa la ventana principal de la aplicación
    app = TodoApp(root) # Crea una instancia de la clase TodoApp, pasando la ventana principal (root) como argumento para inicializar la aplicación de lista de tareas
    root.mainloop() # Inicia el bucle principal de la aplicación, lo que permite que la ventana se mantenga abierta y responda a las interacciones del usuario hasta que se cierre la aplicación