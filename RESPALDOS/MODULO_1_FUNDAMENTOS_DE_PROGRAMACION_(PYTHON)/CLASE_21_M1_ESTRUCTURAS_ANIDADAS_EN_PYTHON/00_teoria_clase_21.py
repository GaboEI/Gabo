#========================================================================================================================================
"""
!CLASE 21  Estructuras Anidadas en Python
?🧩 Objetivo General de la Clase:

Comprender cómo utilizar estructuras de datos anidadas** (listas de diccionarios, diccionarios de listas y más) para
representar datos complejos de forma organizada y profesional.

!📋 Estructura de la clase:
Tendremos 4 ejercicios prácticos, cada uno enfocado en un tipo de estructura anidada:
*🔸 Ejercicio 1 01_directorio_empleados.py
Objetivo: Crear una lista de diccionarios, donde cada diccionario representa a un empleado con sus datos (nombre, edad, 
puesto, habilidades). Luego, mostrar la información con un recorrido adecuado.

*🔸 Ejercicio 2  02_agenda_de_contactos.py
Objetivo: Crear un diccionario donde las claves sean categorías de contacto ("amigos", "familia", "trabajo") y los valores
sean listas de nombres. Agregar nuevos contactos, buscar y mostrar según categoría.

*🔸 Ejercicio 3  03_gestion_usuarios.py
Objetivo: Crear un diccionario donde cada clave sea un ID de usuario, y el valor otro diccionario con nombre, estado 
(activo/inactivo), y lista de permisos. Aplicar búsquedas y actualizaciones.

*🔸 Ejercicio 4  04_reporte_de_ventas.py
Objetivo**: Simular un sistema que almacena ventas por día. Usar una lista de diccionarios, donde cada diccionario contiene 
el nombre del vendedor, total vendido y lista de productos vendidos. Mostrar totales por vendedor y día.

!🧠 Teoría Profunda  Estructuras Anidadas

?🔷 1. ¿Qué son?
Las estructuras anidadas en programación permiten organizar información que por sí sola no se puede representar con una sola 
lista o un solo diccionario. Una estructura anidada es básicamente una estructura dentro de otra:

* Lista que contiene diccionarios
* Diccionario que contiene listas
* Diccionario de diccionarios
* Lista de listas

Este tipo de estructuras es la base para:

* Bases de datos en memoria
* Formatos como JSON
* Almacenes de usuarios, inventarios, catálogos, reportes
#========================================================================================================================================
!🔷 2. Ejemplo real: lista de diccionarios
"""
personas = [
    {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"},
    {"nombre": "Luis", "edad": 25, "ciudad": "Barcelona"}
]


#todo-> Aquí tienes una lista (`[...]`) que contiene varios diccionarios (`{...}`), cada uno con la información de una persona.

#✔ Acceder al nombre de la primera persona:
personas[0]["nombre"]  # Devuelve: "Ana"

#✔ Recorrer e imprimir todos los nombres:
for persona in personas:
    print(persona["nombre"])

#! 🔷 3. Diccionario de listas
asignaturas = {
    "Matemáticas": ["Álgebra", "Cálculo", "Estadística"],
    "Lengua": ["Gramática", "Redacción"]
}

#✔ Acceder al segundo tema de Matemáticas:
asignaturas["Matemáticas"][1]  # Devuelve: "Cálculo"

#✔ Agregar un nuevo tema:
asignaturas["Lengua"].append("Ortografía")

#! 🔷 4. Diccionario de diccionarios

usuarios = {
    "admin01": {"nombre": "Carlos", "activo": True},
    "user02": {"nombre": "Lucía", "activo": False}
}

#✔ Acceder al estado del usuario “user02”:
usuarios["user02"]["activo"]  # Devuelve: False
"""
!🔷 5. Buenas prácticas
* Usar nombres claros para las claves
* Documentar la estructura si es compleja
* Evitar niveles de anidación muy profundos sin justificación
* Para acceder, imprime paso por paso si da error

!🔷 6. Aplicación profesional
?En el mundo real, verás estructuras anidadas en:
* Archivos JSON/API (respuesta de servicios web)
* Formularios web que se traducen a objetos complejos
* Sistemas de usuarios, ventas, inventarios
* Automatización de informes jerárquicos

Aprender esto te permite trabajar con APIs, bases de datos y estructuras complejas que encontrarás 
constantemente en empresas.
"""
#========================================================================================================================================
