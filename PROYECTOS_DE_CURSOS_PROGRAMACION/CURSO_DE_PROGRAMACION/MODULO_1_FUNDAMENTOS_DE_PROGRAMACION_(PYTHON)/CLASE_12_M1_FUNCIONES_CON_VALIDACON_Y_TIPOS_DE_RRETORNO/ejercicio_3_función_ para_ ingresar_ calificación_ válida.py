#-----------------------------------------------------------------------------------------
"""
#!🧪 EJERCICIO 3 CLASE 12
#?📌 Nombre: “Función para ingresar calificación válida (0 a 10)”
#?🔑 Concepto clave: Validación de rango + tipos + retorno seguro

#todo 🎯 ¿Qué debes lograr?
#? Crear una función que:
1️⃣ Solicite al usuario una calificación.
2️⃣ Verifique que sea un número válido entre 0 y 10.
3️⃣ Devuelva ese número solo si es válido.
4️⃣ En caso de error (texto, número negativo, mayor que 10, etc), lo indique y devuelva None.

#!📌 Detalles clave
✅ Debes usar try/except para atrapar errores si el usuario ingresa letras.
✅ El número puede tener decimales (7.5 es válido).
✅ No aceptes nada fuera del rango 0 <= x <= 10.
#!💼 Vida profesional: ¿Dónde usar esto?
- Evaluación de notas escolares.
- Ponderaciones en encuestas y escalas de satisfacción.
- Puntuaciones para sistemas de calificación (como estrellas o reviews).
"""
#-----------------------------------------------------------------------------------------  
def pedir_calificacion():
    while True:
        nombre = input("Ingrese el nombre del usuario: ").strip().capitalize()
        if all(p.isalpha() for p in nombre.strip()):
            break
        else:
            print("Hmm... Recuerda que el nombre debe tener solo letras. Nada de números o signos. 😊")

    try:        
        clasificacion = float(input(f" Estimado, {nombre} ingrese la clasificacion  de [0/10] "))
        if 0 <= clasificacion <= 10:
            return nombre, clasificacion
        else:
            return nombre, None
    except ValueError:
        return nombre, None

nombre, clasificacion = pedir_calificacion()

if clasificacion is not None:
    print(f"🟢 {nombre} su clasificacion fue registrada con exito")
else:
    print(f"🔴 {nombre}, calificación inválida. Debe estar entre 0 y 10.")
