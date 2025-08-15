import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Lista para almacenar los eventos
events = []

# Función para agregar evento
def add_event():
    name = name_entry.get()
    desc = desc_entry.get()
    date = date_entry.get()

    if not name or not desc or not date:
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
        return

    try:
        datetime.strptime(date, "%Y-%m-%d %H:%M")  # Valida formato
    except ValueError:
        messagebox.showerror("Formato de fecha incorrecto", "Usa el formato: YYYY-MM-DD HH:MM")
        return

    events.append((name, desc, date, "Pending"))
    messagebox.showinfo("Evento agregado", f"✅ Evento '{name}' agregado correctamente.")

    # Limpiar campos
    name_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

# Ventana principal
root = tk.Tk()
root.title("Agenda Personal")

# Campos de entrada
tk.Label(root, text="Nombre del evento:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Descripción:").pack()
desc_entry = tk.Entry(root)
desc_entry.pack()

tk.Label(root, text="Fecha (YYYY-MM-DD HH:MM):").pack()
date_entry = tk.Entry(root)
date_entry.pack()

# Botón para agregar evento
tk.Button(root, text="Agregar Evento", command=add_event).pack(pady=10)

# Ejecutar ventana
root.mainloop()