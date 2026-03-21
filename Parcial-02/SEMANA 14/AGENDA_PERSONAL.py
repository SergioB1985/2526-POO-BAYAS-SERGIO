import tkinter as tk # Biblioteca para crear interfaces gráficas
from tkinter import ttk, messagebox # Biblioteca para tablas y mensajes
from tkcalendar import DateEntry # Biblioteca para seleccionar fechas

# Lista para almacenar eventos
eventos = []


# Función para agregar evento
def agregar_evento():
    fecha = entry_fecha.get() # Obtener fecha del DateEntry
    hora = entry_hora.get() # Obtener hora del Entry
    descripcion = entry_descripcion.get() # Obtener descripción del Entry

    if fecha == "" or hora == "" or descripcion == "": # Validar que no haya campos vacíos
        messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos") # Mostrar mensaje de advertencia
        return

    evento = (fecha, hora, descripcion) # Crear tupla con los datos del evento
    eventos.append(evento) # Agregar evento a la lista

    actualizar_tabla() # Actualizar tabla para mostrar el nuevo evento

    # Limpiar campos
    entry_hora.delete(0, tk.END) # Limpiar campo de hora
    entry_descripcion.delete(0, tk.END) # Limpiar campo de descripción


# Función para actualizar tabla
def actualizar_tabla(): # Función que limpia tablas antes de actualizar
    for fila in tree.get_children(): # Obtener todas las filas de la tabla
        tree.delete(fila) # Eliminar cada fila de la tabla

    for evento in eventos: # Agregar cada evento de la lista a la tabla
        tree.insert("", tk.END, values=evento) # Insertar evento en la tabla con sus valores (fecha, hora, descripción)


# Función para eliminar evento
def eliminar_evento():
    seleccionado = tree.selection()

    if not seleccionado: # Validar que se haya seleccionado un evento para eliminar
        messagebox.showwarning("Selección vacía", "Seleccione un evento para eliminar")
        return

    confirmacion = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento seleccionado?")

    if confirmacion: # Si el usuario confirma la eliminación, se procede a eliminar el evento seleccionado
        for item in seleccionado: # Iterar sobre los eventos seleccionados (puede ser más de uno)
            valores = tree.item(item, "values")
            eventos.remove(valores)
            tree.delete(item)


# Ventana principal
ventana = tk.Tk() # Crear ventana principal
ventana.title("Agenda Personal") # Establecer título de la ventana
ventana.geometry("600x400") # Establecer tamaño de la ventana (ancho x alto)

# ===== FRAME DE LISTA =====
frame_lista = tk.Frame(ventana)# Crear un frame para contener la tabla de eventos
frame_lista.pack(pady=10) # Empaquetar el frame con un margen vertical de 10 píxeles

# Treeview
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings") # Crear un Treeview con columnas para fecha, hora y descripción, y mostrar solo los encabezados

tree.heading("Fecha", text="Fecha") # Establecer encabezado de la columna "Fecha"
tree.heading("Hora", text="Hora") # Establecer encabezado de la columna "Hora"
tree.heading("Descripción", text="Descripción") # Establecer encabezado de la columna "Descripción"

tree.column("Fecha", width=100) # Establecer ancho de la columna "Fecha"
tree.column("Hora", width=80) # Establecer ancho de la columna "Hora"
tree.column("Descripción", width=250) # Establecer ancho de la columna "Descripción"

tree.pack() # Empaquetar el Treeview para que se muestre en la ventana

# ===== FRAME DE ENTRADA =====
frame_entrada = tk.Frame(ventana) # Crear un frame para contener los campos de entrada de datos (fecha, hora, descripción)
frame_entrada.pack(pady=10) # Empaquetar el frame con un margen vertical de 10 píxeles

# Fecha
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5) # Crear etiqueta para el campo de fecha y ubicarla en la primera fila y primera columna del grid con un margen de 5 píxeles
entry_fecha = DateEntry(frame_entrada, date_pattern='Y-m-d') # Crear un DateEntry para seleccionar la fecha, con el formato de fecha "año-mes-día"
entry_fecha.grid(row=0, column=1, padx=5, pady=5) # Ubicar el DateEntry en la primera fila y segunda columna del grid con un margen de 5 píxeles

# Hora
tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5) # Crear etiqueta para el campo de hora y ubicarla en la segunda fila y primera columna del grid con un margen de 5 píxeles
entry_hora = tk.Entry(frame_entrada) # Crear un Entry para ingresar la hora del evento
entry_hora.grid(row=1, column=1, padx=5, pady=5) # Ubicar el Entry de hora en la segunda fila y segunda columna del grid con un margen de 5 píxeles

# Descripción
tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5) # Crear etiqueta para el campo de descripción y ubicarla en la tercera fila y primera columna del grid con un margen de 5 píxeles
entry_descripcion = tk.Entry(frame_entrada, width=40) # Crear un Entry para ingresar la descripción del evento, con un ancho de 40 caracteres
entry_descripcion.grid(row=2, column=1, padx=5, pady=5) # Ubicar el Entry de descripción en la tercera fila y segunda columna del grid con un margen de 5 píxeles

# ===== FRAME DE BOTONES =====
frame_botones = tk.Frame(ventana) # Crear un frame para contener los botones de acción (agregar, eliminar, salir)
frame_botones.pack(pady=10) # Empaquetar el frame con un margen vertical de 10 píxeles

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento) # Crear un botón para agregar eventos, con el texto "Agregar Evento" y asignar la función "agregar_evento" como comando a ejecutar al hacer clic en el botón
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento) # Crear un botón para eliminar eventos seleccionados, con el texto "Eliminar Evento Seleccionado" y asignar la función "eliminar_evento" como comando a ejecutar al hacer clic en el botón
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", command=ventana.quit) # Crear un botón para salir de la aplicación, con el texto "Salir"
btn_salir.grid(row=0, column=2, padx=10)
# Ejecutar app
ventana.mainloop() # Iniciar el bucle principal de la aplicación para que la ventana se mantenga abierta y responda a las interacciones del usuario