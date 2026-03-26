import tkinter as tk # Librería para la interfaz gráfica
from tkinter import messagebox # Librería para mostrar mensajes emergentes

class TodoApp: # Clase principal de la aplicación de lista de tareas
    def __init__(self, root): # Metodo constructor que inicializa la interfaz y los componentes
        self.root = root # Referencia a la ventana principal
        self.root.title("Lista de Tareas") # Título de la ventana
        self.root.geometry("420x480") # Tamaño de la ventana

        self.tasks = []  # Lista interna de tareas

        # Campo de entrada
        self.entry = tk.Entry(root, width=32) # Campo de texto para ingresar nuevas tareas
        self.entry.pack(pady=10) # Empaquetar el campo de entrada con un margen vertical
        self.entry.bind("<Return>", self.add_task_event)  # Enter agrega tarea

        # Botones
        frame_buttons = tk.Frame(root) # Marco para contener los botones y organizarlos horizontalmente
        frame_buttons.pack(pady=10) # Empaquetar el marco de botones con un margen vertical

        self.btn_add = tk.Button(frame_buttons, text="Añadir Tarea", command=self.add_task) # Botón para añadir tareas
        self.btn_add.grid(row=0, column=0, padx=5) # Posicionar el botón de añadir en la primera columna del marco con un margen horizontal

        self.btn_complete = tk.Button(frame_buttons, text="Marcar como Completada", command=self.complete_task) # Botón para marcar tareas como completadas
        self.btn_complete.grid(row=0, column=1, padx=5) # Posicionar el botón de completar en la segunda columna del marco con un margen horizontal

        self.btn_delete = tk.Button(frame_buttons, text="Eliminar Tarea", command=self.delete_task) # Botón para eliminar tareas
        self.btn_delete.grid(row=0, column=2, padx=5) # Posicionar el botón de eliminar en la tercera columna del marco con un margen horizontal

        # Botón salir
        self.btn_exit = tk.Button(root, text="Salir", command=self.exit_app, bg="red", fg="white") # Botón para salir de la aplicación con un fondo rojo y texto blanco
        self.btn_exit.pack(pady=5) # Empaquetar el botón de salir con un margen vertical

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=48, height=15) # Lista para mostrar las tareas con un ancho de 48 caracteres y una altura de 15 líneas
        self.listbox.pack(pady=10) # Empaquetar la lista de tareas con un margen vertical

        # Evento opcional: doble clic para completar tarea
        self.listbox.bind("<Double-Button-1>", self.complete_task_event) # Vincular el evento de doble clic en la lista para marcar tareas como completadas

    def add_task(self): # Función para añadir una nueva tarea a la lista
        task = self.entry.get().strip() # Obtener el texto ingresado en el campo de entrada y eliminar espacios en blanco al inicio y al final
        if task == "": # Verificar si el campo de entrada está vacío
            messagebox.showwarning("Advertencia", "Debe escribir una tarea") # Mostrar una advertencia si el campo de entrada está vacío
            return

        self.tasks.append({"text": task, "completed": False}) # Agregar la nueva tarea a la lista interna de tareas como un diccionario con el texto de la tarea y un estado de completada
        self.update_listbox() # Actualizar la lista de tareas en la interfaz gráfica para reflejar la nueva tarea añadida
        self.entry.delete(0, tk.END) # Limpiar el campo de entrada después de añadir la tarea

    def add_task_event(self, event): # Función para manejar el evento de presionar la tecla Enter en el campo de entrada para añadir una tarea
        self.add_task() # Llamar a la función add_task para añadir la tarea cuando se presiona Enter

    def complete_task(self): # Función para marcar una tarea como completada
        try:
            index = self.listbox.curselection()[0] # Obtener el índice de la tarea seleccionada en la lista
            if self.tasks[index]["completed"]: # Verificar si la tarea ya está marcada como completada
                messagebox.showinfo("Información", "Esta tarea ya está marcada como completada")
            else:
                self.tasks[index]["completed"] = True
                self.update_listbox()
                messagebox.showinfo("Éxito", "Tarea marcada como completada")
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea")

    def complete_task_event(self, event): # Función para manejar el evento de doble clic en la lista para marcar una tarea como completada
        self.complete_task() # Llamar a la función complete_task para marcar la tarea como completada cuando se hace doble clic en ella

    def delete_task(self): # Función para eliminar una tarea de la lista
        try:
            index = self.listbox.curselection()[0] # Obtener el índice de la tarea seleccionada en la lista
            del self.tasks[index] # Eliminar la tarea de la lista interna de tareas utilizando el índice obtenido
            self.update_listbox() # Actualizar la lista de tareas en la interfaz gráfica para reflejar la eliminación de la tarea
        except IndexError: # Manejar el caso en que no se haya seleccionado ninguna tarea para eliminar
            messagebox.showwarning("Advertencia", "Seleccione una tarea")

    def exit_app(self): # Función para salir de la aplicación con una confirmación
        confirm = messagebox.askyesno("Salir", "¿Está seguro que desea salir de la aplicación?") # Mostrar un cuadro de diálogo de confirmación para salir de la aplicación
        if confirm: # Si el usuario confirma que desea salir, cerrar la ventana principal de la aplicación
            self.root.destroy() # Cerrar la ventana principal de la aplicación

    def update_listbox(self): # Función para actualizar la lista de tareas en la interfaz gráfica
        self.listbox.delete(0, tk.END) # Limpiar la lista de tareas en la interfaz gráfica antes de actualizarla con las tareas actuales
        for task in self.tasks: # Iterar sobre cada tarea en la lista interna de tareas y agregarla a la lista de tareas en la interfaz gráfica
            if task["completed"]: # Si la tarea está marcada como completada, agregar un símbolo de verificación antes del texto de la tarea para indicar que está completada
                self.listbox.insert(tk.END, "✔ " + task["text"]) # Agregar la tarea a la lista de tareas en la interfaz gráfica con un símbolo de verificación para indicar que está completada
            else:
                self.listbox.insert(tk.END, task["text"]) # Agregar la tarea a la lista de tareas en la interfaz gráfica sin un símbolo de verificación para indicar que no está completada


if __name__ == "__main__": # Punto de entrada del programa, se ejecuta cuando se ejecuta el script directamente
    root = tk.Tk() # Crear la ventana principal de la aplicación utilizando la clase Tk de la biblioteca tkinter
    app = TodoApp(root) # Crear una instancia de la clase TodoApp, pasando la ventana principal como argumento para inicializar la aplicación de lista de tareas
    root.mainloop() # Iniciar el bucle principal de la interfaz gráfica para que la aplicación se mantenga abierta y responda a las interacciones del usuario