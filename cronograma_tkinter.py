import tkinter as tk
from tkinter import messagebox

# ------------------------
# 🧠 Diccionario de clases por curso
# ------------------------
cursos_clases = {
    "Curso de Programación Base (Python)": [
        "Tipos de datos: int, float, str, bool", "Variables y constantes", "Operadores aritméticos y lógicos",
        "Estructuras de control: if, elif, else", "Bucles: for, while", "Funciones",
        "Manejo de errores (try, except)", "Manejo de archivos (lectura, escritura)",
        "Estructuras de datos: listas, diccionarios, tuplas, sets", "Proyecto: Gestor de tareas con archivos",
        "Funciones: def, argumentos, retorno", "Funciones con validación", "Parámetros opcionales",
        "Manejo de errores avanzado", "Archivos: open, read, write", "Escritura/lectura de archivos",
        "Proyecto: Registro de notas", "Manipulación de strings", "Pensamiento algorítmico",
        "Modularización", "Estructuras anidadas", "Proyecto: Agenda de eventos",
        "Condiciones lógicas complejas", "Buenas prácticas de estilo", "Trabajo con fechas",
        "Condicionales anidadas", "Validación de entradas", "Proyecto: Sistema de votación",
        "Repaso general", "Evaluación del módulo"
    ],
    "Curso de JavaScript": [
        "Introducción a JavaScript", "`var`, `let`, `const`", "Tipos de datos primitivos",
        "Operadores: aritméticos y lógicos", "Condicionales: if, else, switch", "Bucles: for, while, do while",
        "Funciones: declaración y expresión", "Arrow functions", "Proyecto: Conversor de divisas",
        "Evaluación módulo 1", "Arrays y métodos", "Objetos y notación punto",
        "Funciones dentro de objetos", "Clases y prototipos", "Manipulación del DOM",
        "Eventos y listeners", "Timers y asincronía", "Fetch API y promesas", "Async/await",
        "Proyecto: To-Do List", "Evaluación módulo 2", "Repaso final"
    ],
    "Curso de HTML, CSS y SQL": [
        "Introducción a HTML", "Listas, enlaces e imágenes", "Tablas y formularios",
        "Etiquetas semánticas", "Multimedia", "Metaetiquetas SEO", "Atributos globales",
        "Formularios: inputs, selects", "Validaciones nativas", "Proyecto: Formulario accesible",
        "Nuevas etiquetas HTML5", "Buenas prácticas HTML", "Landing Page semántica", "SEO avanzado",
        "Evaluación HTML", "Selectores en CSS", "Unidades, colores, tipografías", "Espaciado y texto",
        "Box model", "Flexbox y Grid", "Position y Z-index", "Media queries", "Tarjeta de producto",
        "Animaciones CSS", "Evaluación CSS", "SQL: estructura y SELECT", "JOINS y relaciones",
        "Funciones SQL", "Consultas avanzadas", "Evaluación SQL"
    ],
    "Curso de Desarrollo Web Full Stack": [
        "Instalación y entorno", "Terminal y pip", "DevTools y VSCode", "HTML5 básico",
        "Formularios y estructura semántica", "CSS: selectores y box model", "Flexbox y Grid",
        "Diseño responsive con media queries", "Landing Page práctica", "Python para web",
        "Flask: estructura y rutas", "Formularios con Flask", "CRUD en Flask",
        "Autenticación básica", "Base de datos con SQLAlchemy", "Proyecto: blog personal",
        "Pruebas con pytest", "Docker y entorno", "Despliegue VPS/Render", "Git y control de versiones",
        "APIs REST", "Autenticación con JWT", "Testing avanzado", "Proyecto final", "Evaluación"
    ],
    "Curso de C++": [
        "Historia y compilación", "Tipos de datos", "Variables y buenas prácticas",
        "Entrada y salida", "Operadores", "Condicionales", "Bucles", "Funciones básicas",
        "Paso por valor y referencia", "Arrays", "Strings", "Punteros", "Referencias",
        "Memoria dinámica", "Struct y organización de datos", "Enumeraciones",
        "STL básico", "Proyecto: agenda", "Errores con try-catch", "Proyecto: calculadora",
        "Archivos .h y .cpp", "Evaluación final", "Repaso punteros", "Vector avanzado", "Final módulo"
    ],
    "Curso de Java/Kotlin": [
        "Historia y entorno", "Estructura básica", "Tipos de datos", "Variables y convenciones",
        "Operadores", "Casting y parse", "Entrada por consola", "Condicionales", "Switch",
        "Bucles", "For-each y bucles anidados", "Break y continue", "Arreglos", "Métodos",
        "Sobrecarga", "Try-catch", "ArrayList", "Proyecto: calculadora", "Buenas prácticas",
        "Evaluación final"
    ],
    "Curso de C#": [
        "Historia y VS Code", "Primer programa", "Tipos de datos", "Variables y constantes",
        "Operadores", "Casting", "Entrada/Salida", "Estructura limpia", "Condicionales",
        "Switch", "Bucles", "Break y continue", "Proyecto: calculadora", "Arreglos",
        "Métodos", "Parámetros ref y out", "Métodos con validación", "Proyecto: gestor de notas",
        "Try-catch", "List<T>", "Proyecto final", "Buenas prácticas", "Evaluación final",
        "Repaso general", "Finalización"
    ],
    "Curso de Tkinter (Python visual)": [
        "Primera ventana", "Etiquetas y botones", "Layouts: pack, grid", "Interacción básica",
        "Proyecto: calculadora visual", "Convertir gestor a GUI", "Checkboxes y estados",
        "Formulario de estudiantes", "Registro con validaciones", "Listbox",
        "Radiobutton y menús", "MessageBox", "Estilos con ttk", "Proyecto: Agenda visual"
    ],
    "Curso de Seguridad Informática": [
        "Introducción a seguridad informática", "Principios de confidencialidad", "Tipos de amenazas",
        "Tipos de hackers", "Marco legal", "Ataques comunes", "Autenticación y autorización",
        "Contraseñas seguras", "Antivirus y antimalware", "Firewalls", "IDS/IPS",
        "Criptografía básica", "Protocolos seguros", "Wi-Fi segura", "VPN",
        "Ingeniería social", "Seguridad en móviles y correos", "Backups", "Políticas de seguridad",
        "Análisis de vulnerabilidades", "Caso real de ciberataque", "Buenas prácticas",
        "Herramientas gratuitas", "Pentesting básico", "Evaluación final"
    ]
}

# ------------------------
# 📅 Distribución escalonada por día
# ------------------------
plan_diario = [
    (1, "Curso de Programación Base (Python)", 1),
    (25, "Curso de Tkinter (Python visual)", 1),
    (41, "Curso de JavaScript", 1),
    (70, "Curso de HTML, CSS y SQL", 1),
    (100, "Curso de Desarrollo Web Full Stack", 1),
    (151, "Curso de C++", 1),
    (191, "Curso de Java/Kotlin", 1),
    (236, "Curso de C#", 1),
    (276, "Curso de Seguridad Informática", 1),
]

# ------------------------
# 🔁 Generar cronograma
# ------------------------
cronograma_dia = {}
progreso = {curso: 0 for curso in cursos_clases}

for dia in range(1, 341):
    tareas = []
    for inicio, curso, clases_por_dia in plan_diario:
        if dia >= inicio and progreso[curso] < len(cursos_clases[curso]):
            for _ in range(clases_por_dia):
                if progreso[curso] < len(cursos_clases[curso]):
                    n = progreso[curso]
                    tareas.append((curso, n + 1, cursos_clases[curso][n]))
                    progreso[curso] += 1
    cronograma_dia[dia] = tareas

# ------------------------
# 🖼️ Interfaz Tkinter
# ------------------------
def buscar_dia():
    try:
        dia = int(entry_dia.get())
        if dia < 1 or dia > 340:
            raise ValueError("El día debe estar entre 1 y 340.")
        tareas = cronograma_dia.get(dia, [])
        if not tareas:
            resultado = f"📅 Día {dia}:\nNo tienes clases asignadas."
        else:
            resultado = f"📅 Día {dia}:\n"
            for curso, clase_nro, clase_nombre in tareas:
                resultado += f"\n🏨 Curso: {curso}\n📚 Tema:\n- Clase {clase_nro}: {clase_nombre}\n"
        messagebox.showinfo("Agenda de estudio", resultado)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Crear GUI
ventana = tk.Tk()
ventana.title("📚 Cronograma de Estudios con Gabo")
label = tk.Label(ventana, text="📅 Ingresa el número del día (1–340):")
label.pack(pady=10)

entry_dia = tk.Entry(ventana)
entry_dia.pack(pady=5)

boton = tk.Button(ventana, text="Consultar Día", command=buscar_dia)
boton.pack(pady=10)

ventana.mainloop()