import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# Crear cronograma
def crear_cronograma():
    fecha_inicio = datetime.strptime("2025-07-26", "%Y-%m-%d")
    cursos = [
        {"nombre": "Curso de Programación Base (Python)", "duracion_dias": 40, "horas_dia": 6},
        {"nombre": "Curso de JavaScript", "duracion_dias": 45, "horas_dia": 6},
        {"nombre": "Curso de Desarrollo Web Full Stack", "duracion_dias": 50, "horas_dia": 6},
        {"nombre": "Curso de HTML, CSS y SQL", "duracion_dias": 30, "horas_dia": 6},
        {"nombre": "Curso de C++", "duracion_dias": 40, "horas_dia": 6},
        {"nombre": "Curso de Java/Kotlin", "duracion_dias": 45, "horas_dia": 6},
        {"nombre": "Curso de C#", "duracion_dias": 40, "horas_dia": 6},
        {"nombre": "Curso de Tkinter con Python", "duracion_dias": 20, "horas_dia": 6},
        {"nombre": "Curso de Seguridad Informática", "duracion_dias": 30, "horas_dia": 6},
    ]
    cronograma = []
    fecha_actual = fecha_inicio
    for curso in cursos:
        for _ in range(curso["duracion_dias"]):
            cronograma.append({
                "Fecha": fecha_actual.strftime("%Y-%m-%d"),
                "Curso": curso["nombre"],
                "Horas": curso["horas_dia"]
            })
            fecha_actual += timedelta(days=1)
    return cronograma

# Función para mostrar el cronograma del día solicitado
def buscar_dia():
    try:
        dia = int(entry_dia.get())
        if dia < 1 or dia > len(cronograma):
            raise ValueError("Día fuera de rango (1 a {}).".format(len(cronograma)))
        datos = cronograma[dia - 1]
        resultado = f"📅 Día {dia}:\n📌 Fecha: {datos['Fecha']}\n📘 Curso: {datos['Curso']}\n⏱️ Horas: {datos['Horas']}h"
        messagebox.showinfo("Cronograma del Día", resultado)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI con Tkinter
cronograma = crear_cronograma()
ventana = tk.Tk()
ventana.title("Cronograma Diario de Gabo")

label = tk.Label(ventana, text="📘 Ingresa el número del día que quieres consultar:")
label.pack(pady=10)

entry_dia = tk.Entry(ventana)
entry_dia.pack(pady=5)

boton = tk.Button(ventana, text="📅 Consultar Día", command=buscar_dia)
boton.pack(pady=10)

ventana.mainloop()