#-------------------------------------------------------------------------------------
"""
#!🧠 CLASE 12  Funciones con validación y retorno condicional
Ejercicio 2
📌 Nombre del ejercicio: “Sumar solo si ambos números son válidos”
🔑 Concepto: return condicional y control de flujo con validaciones.

#todo 🧪 Teoría previa: return condicional + validación de entradas

En Python, una función puede decidir si devuelve un valor o no, dependiendo de 
ciertas condiciones. Esto permite controlar qué hacer si los datos no son válidos.
#-------------------------------------------------------------------------------------
#! 🧱 Estructura esperada del ejercicio
#? Vas a construir una función que:
1️⃣ Reciba dos valores ingresados por el usuario.
2️⃣ Verifique si ambos son números enteros válidos.
3️⃣ Si son válidos, retorne la suma.
4️⃣ Si alguno no es válido, retorne None o un mensaje de error.
5️⃣ uego, usando if, decides qué mostrarle al usuario.
"""
#-------------------------------------------------------------------------------------
def sumar_si_validos(a, b):
    if type(a) == int and type(b) == int: # Verifica si ambos parámetros son enteros
        return a + b # Si son enteros, retorna la suma de #!(a y b)
    else:
        return None # Si no son ambos enteros, retorna #!None

#? Solicitar al usuario los datos
valor1 = input("Igrese el primer valor: ")
valor2 = input("Ingrese el segundo valor: ")

#? Convertir e intentar sumar
try:
    num1 = int(valor1)
    num2 = int(valor2)
    resultado = sumar_si_validos(num1, num2) # Llama a la función con los valores convertidos y guarda el resultado

    if resultado is not None: # Verifica si el resultado no es None (es decir, si la suma fue válida)
        print(f"🟢 La suma es: {resultado}")
    else:
        print("🔴 Error! Alguno de los datos no son validos")

except ValueError: # Captura cualquier error
    print("❌ Error! Debes ingresar solo numeros enteros")
#-------------------------------------------------------------------------------------