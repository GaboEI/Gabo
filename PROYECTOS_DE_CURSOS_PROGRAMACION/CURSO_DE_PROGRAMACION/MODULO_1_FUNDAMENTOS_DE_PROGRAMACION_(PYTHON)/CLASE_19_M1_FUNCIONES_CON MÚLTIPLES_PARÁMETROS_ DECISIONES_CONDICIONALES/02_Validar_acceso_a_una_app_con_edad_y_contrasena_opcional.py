#===================================================================================================================
"""
#!🧱 EJERCICIO 2  CLASE 19
#*📌 Objetivo: Validar si un usuario puede acceder a una app, según su edad y contraseña

#?🎯 ¿Qué debe hacer el script?
1️⃣ Definir una función validar_acceso() con 2 parámetros:
====edad (obligatorio)
====clave (opcional, valor por defecto: "0000")
2️⃣ Si el usuario tiene menos de 18 años, negar acceso automáticamente
3️⃣ Si tiene 18 o más y la clave es "admin", permitir el acceso
4️⃣ En cualquier otro caso, mostrar mensaje de acceso denegado
5️⃣ Retornar un mensaje claro según el resultado
6️⃣ Mostrar 2 o 3 pruebas llamando la función
"""
#===================================================================================================================
def validar_acceso(edad: int, clave: str = "0000" ) -> str:
    if edad < 18:
        return "🚫 Acceso DENEGADO, por favor espere tener al menos 18 años para acceder"
    elif clave == "admin":
        return "❇️ Acceso PERMITIDO ¡Bienvenido!"
    else:
        return "❌ Acceso DENEGADO, clave incorecta"

print(f"Caso 1 (menor de edad): {validar_acceso(16)}")
print(f"Caso 2 (mayor de edad, clave por defecto): {validar_acceso(20)}")
print(f"Caso 3 (mayor de edad, clave 'admin'): {validar_acceso(25, "admin")}")
print(f"Caso 4 (mayor de edad, clave 'erronea'): {validar_acceso(30, "220285")}")
print(f"Caso 5 (menor de edad, clave 'admin')  {validar_acceso(17,"admin")}")
#===================================================================================================================
#!RESPUESTA DE LA CONSOLA EJEMPLO RREALIZADO:
"""
Caso 1 (menor de edad): 🚫 Acceso DENEGADO, por favor espere tener al menos 18 años para acceder
Caso 2 (mayor de edad, clave por defecto): ❌ Acceso DENEGADO, clave incorecta
Caso 3 (mayor de edad, clave 'admin'): ❇️ Acceso PERMITIDO ¡Bienvenido!
Caso 4 (mayor de edad, clave 'erronea'): ❌ Acceso DENEGADO, clave incorecta
Caso 5 (menor de edad, clave 'admin')  🚫 Acceso DENEGADO, por favor espere tener al menos 18 años para acceder
"""
#===================================================================================================================
