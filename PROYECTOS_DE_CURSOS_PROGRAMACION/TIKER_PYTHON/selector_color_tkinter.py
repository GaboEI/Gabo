# selector_color_tkinter.py

import tkinter as tk  #1️⃣ Importamos Tkinter
from tkinter import ttk  #2️⃣ Importamos ttk para widgets modernos

#3️⃣ Lista de colores en formato {Nombre: Código HEX}
colores = {
    "Celeste claro": "#E0FFFF",
    "Beige suave": "#F5F5DC",
    "Gris neutro": "#F0F0F0",
    "Rosa fuerte": "#FF69B4",
    "Verde pastel": "#C1E1C1",
    "Rojo alerta": "#DC3545",
    "Azul clásico": "#007BFF"
}

#4️⃣ Función que cambia el color de fondo
def cambiar_color():
    seleccion = color_var.get()             #5️⃣ Obtenemos el nombre seleccionado
    color = colores[seleccion]              #6️⃣ Obtenemos su código HEX
    ventana.configure(bg=color)             #7️⃣ Aplicamos el color al fondo

#8️⃣ Crear ventana principal
ventana = tk.Tk()
ventana.title("Selector de color visual")
ventana.geometry("400x200")

#9️⃣ Variable para opción seleccionada
color_var = tk.StringVar(value=list(colores.keys())[0])

#🔟 Etiqueta de instrucción
label = ttk.Label(ventana, text="Selecciona un color para el fondo:")
label.pack(pady=10)

#🔟 Menú desplegable con los colores
selector = ttk.OptionMenu(ventana, color_var, color_var.get(), *colores.keys())
selector.pack(pady=5)

#🔟 Botón para aplicar el color
boton = ttk.Button(ventana, text="Aplicar color", command=cambiar_color)
boton.pack(pady=10)

ventana.mainloop()
