import tkinter as tk # Importa la biblioteca tkinter y la asigna al alias tk para facilitar su uso en el código
from tkinter import messagebox # Importa el módulo messagebox de tkinter para mostrar cuadros de diálogo de mensajes al usuario, como advertencias, confirmaciones e información


# Función para agregar datos
def agregar():
    texto = entrada.get() # Obtiene el texto ingresado por el usuario en el campo de entrada y lo almacena en la variable texto

    if texto != "": # Verifica si el texto no está vacío, es decir, si el usuario ha ingresado algo en el campo de entrada
        lista.insert(tk.END, texto) # Si el texto no está vacío, se inserta el texto en la lista, con tk.END para agregarlo al final de la lista
        entrada.delete(0, tk.END) # Permite al usuario borrar el contenido del campo de entrada después de agregar el texto a la lista.
        actualizar_botones() # Después de agregar un elemento a la lista, se llama a la función actualizar_botones() para verificar si los botones de eliminar y limpiar deben ser habilitados o deshabilitados según el estado actual de la lista
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato")


# Función eliminar seleccionado
def eliminar_seleccionado():
    seleccion = lista.curselection() # Obtiene el índice del elemento de la lista y lo almacena en la variable seleccion

    if seleccion: # Verificar si hay una selección
        lista.delete(seleccion) # Si hay una selección, se elimina el elemento, pasando el índice de la selección como argumento
        actualizar_botones() # Después de eliminar un elemento de la lista, se llama a la función actualizar_botones() para verificar si los botones de eliminar y limpiar deben ser habilitados o deshabilitados según el estado actual de la lista
    else:
        messagebox.showwarning("Advertencia", "Seleccione un elemento para eliminar") # Si no hay una selección, se muestra un mensaje de advertencia al usuario, indicando que debe seleccionar un elemento para eliminar


# Función limpiar
def limpiar_todo():
    lista.delete(0, tk.END) # Elimina todos los elementos de la lista
    actualizar_botones() # Después de limpiar la lista, se llama a la función actualizar_botones() para verificar si los botones de eliminar y limpiar deben ser habilitados o deshabilitados según el estado actual de la lista (en este caso, estarán deshabilitados porque la lista estará vacía)


# Activar o desactivar botones
def actualizar_botones():
    if lista.size() == 0: # Si la lista está vacía, desactivar botones
        btn_eliminar.config(state="disabled") # Desactiva el botón de eliminar, estableciendo el estado en "disabled"
        btn_limpiar.config(state="disabled") # Desactiva el botón de limpiar, estableciendo el estado en "disabled"
    else:
        btn_eliminar.config(state="normal") # Si la lista no está vacía, habilita el botón de eliminar, estableciendo el estado en "normal"
        btn_limpiar.config(state="normal") # Habilita el botón de limpiar, estableciendo el estado en "normal"


# Función salir con confirmación
def salir():
    respuesta = messagebox.askyesno("Salir del sistema", "¿Desea finalizar el sistema?") # Permite al usuario confirmar si desea salir del sistema

    if respuesta:  # Si el usuario presiona Sí muestra un mensaje de información y cierra la ventana
        messagebox.showinfo("Sistema", "Finalización del sistema") # Muestra un mensaje de información indicando que el sistema se ha finalizado
        ventana.destroy()
    else:
        return


# Ventana principal
ventana = tk.Tk() # Crea la ventana principal de la aplicación
ventana.title("Sistema de Registro de Datos") # Establece el título de la ventana
ventana.geometry("450x330") # Establece el tamaño de la ventana (ancho x alto)

# Etiqueta
label = tk.Label(ventana, text="Ingrese información:") # Crea una etiqueta que indica al usuario que ingrese información
label.pack(pady=5) # Agrega la etiqueta a la ventana y establece un espacio vertical de 5 píxeles alrededor de ella

# Campo de texto
entrada = tk.Entry(ventana, width=35) # Crea un campo de texto para que el usuario ingrese información, con un ancho de 35 caracteres
entrada.pack(pady=5) # Agrega el campo de texto a la ventana y establece un espacio vertical de 5 píxeles alrededor de él

# Lista
lista = tk.Listbox(ventana, width=50, height=10) # Crea una lista para mostrar los datos ingresados por el usuario, con un ancho de 50 caracteres y una altura de 10 líneas
lista.pack(pady=10) # Agrega la lista a la ventana y establece un espacio vertical de 10 píxeles alrededor de ella

# Frame para botones
frame_botones = tk.Frame(ventana) # Crea un contenedor (frame) para organizar los botones en la ventana
frame_botones.pack(pady=10) # Agrega el frame a la ventana y establece un espacio vertical de 10 píxeles alrededor de él

# Botón agregar
btn_agregar = tk.Button(frame_botones, text="Agregar", command=agregar) # Crea un botón para agregar datos a la lista, con el texto "Agregar" y asigna la función agregar() al evento de clic
btn_agregar.grid(row=0, column=0, padx=5) # Agrega el botón al frame de botones y lo posiciona en la fila 0, columna 0, con un espacio horizontal de 5 píxeles entre los botones

# Botón eliminar
btn_eliminar = tk.Button(frame_botones, text="Eliminar seleccionado", command=eliminar_seleccionado, state="disabled") # Crea un botón para eliminar el elemento seleccionado de la lista, con el texto "Eliminar seleccionado", asigna la función eliminar_seleccionado() al evento de clic y lo desactiva inicialmente
btn_eliminar.grid(row=0, column=1, padx=5) # Agrega el botón al frame de botones y lo posiciona en la fila 0, columna 1, con un espacio horizontal de 5 píxeles entre los botones

# Botón limpiar
btn_limpiar = tk.Button(frame_botones, text="Limpiar todo", command=limpiar_todo, state="disabled") # Crea un botón para limpiar toda la lista.
btn_limpiar.grid(row=0, column=2, padx=5) # Agrega el botón al frame de botones y lo posiciona en la fila 0, columna 2, con un espacio horizontal de 5 píxeles entre los botones

# Botón salir
btn_salir = tk.Button(frame_botones, text="Salir", command=salir) # Crea un botón para salir del sistema, con el texto "Salir" y asigna la función salir() al evento de clic
btn_salir.grid(row=0, column=3, padx=5) # Agrega el botón al frame de botones y lo posiciona en la fila 0, columna 3, con un espacio horizontal de 5 píxeles entre los botones

# Ejecutar programa
ventana.mainloop()