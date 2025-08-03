#=====================================================================================================
"""
#!👁️ Clase 1 Crear tu primera ventana

#?🎯 Objetivo:
Aprender a crear una ventana básica con Tkinter, definir su título, tamaño y color de fondo.
Es el primer paso para que cualquier app visual luzca como un “programa real”.

#!✅ 1. Teoría breve: ¿Qué es Tkinter?

⏺️ Tkinter es el módulo oficial de interfaces gráficas (GUI) en Python.
⏺️ Permite crear ventanas, botones, cajas de texto, menús y más.
⏺️ Viene incluido con la mayoría de instalaciones de Python (no hay que instalarlo por separado).

#todo ¿Cómo se estructura una app en Tkinter?
1️⃣ Crear una ventana principal (Tk()).
2️⃣ Configurar su tamaño, título y color.
3️⃣ Iniciar el bucle principal con .mainloop() para que la ventana esté “viva”.
"""
#=====================================================================================================
#? ✅ 2. Script paso a paso
#? A continuación verás el primer código básico.

import tkinter as tk  # 1️⃣ Importamos el módulo tkinter

ventana = tk.Tk()     # 2️⃣ Creamos una ventana principal

ventana.title("Ventana Gabo")  # 3️⃣ Le damos un título

ventana.geometry("600x400")          # 4️⃣ Definimos el tamaño: ancho x alto en píxeles

ventana.configure(bg="#690638")    # 5️⃣ Establecemos el color de fondo #?👉 https://htmlcolorcodes.com/es/

ventana.mainloop()                   # 6️⃣ Iniciamos el bucle principal
"""
#?=====================================================================================================
#!🔍 Explicación línea por línea:
#?=====================================================================================================
#!Línea	                           Explicación

import tkinter as tk	           Importamos la librería tkinter con el alias tk para escribir menos.
tk.Tk()	                           Crea la ventana principal de la aplicación.
.title(...)	                       Cambia el título de la ventana, lo que aparece arriba.
.geometry(...)	                   Define el tamaño inicial de la ventana.
.configure(bg=...)	               Cambia el color del fondo. Puedes usar nombres como "blue", "white", etc.
.mainloop()	                       Este método mantiene abierta la ventana hasta que el usuario la cierre. Sin él, la ventana se cerraría al instante.
#?=====================================================================================================
"""

