# ----------- 1. ¿Qué es una función? -----------
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Se define con la palabra clave `def` seguida del nombre de la función.

# Ejemplo de una función básica
def saludar():
    print("¡Hola, bienvenido a Python!")

# Llamar a la función
saludar()  # Output: ¡Hola, bienvenido a Python!


# ----------- 2. Funciones con parámetros -----------
# Puedes pasar datos a una función mediante parámetros.

def saludar_personalizado(nombre):
    print(f"Hola, {nombre}, bienvenido a Python!")

# Llamar a la función con un argumento
saludar_personalizado("Gabo")  # Output: Hola, Gabo, bienvenido a Python!


# ----------- 3. Funciones con múltiples parámetros -----------
# Puedes definir funciones con más de un parámetro.

def sumar(a, b):
    resultado = a + b
    print(f"La suma de {a} y {b} es {resultado}")

# Llamar a la función con dos argumentos
sumar(3, 5)  # Output: La suma de 3 y 5 es 8


# ----------- 4. Funciones que devuelven valores -----------
# Las funciones pueden devolver valores utilizando la palabra clave `return`.

def multiplicar(a, b):
    return a * b

# Llamar a la función y almacenar el valor devuelto
resultado = multiplicar(4, 5)
print(f"El resultado de la multiplicación es {resultado}")  # Output: El resultado de la multiplicación es 20


# ----------- 5. Parámetros con valores predeterminados -----------
# Puedes definir valores predeterminados para los parámetros.

def saludar_con_default(nombre="invitado"):
    print(f"Hola, {nombre}!")

# Llamar a la función sin argumento usa el valor predeterminado
saludar_con_default()  # Output: Hola, invitado!
# Llamar a la función con un argumento
saludar_con_default("Gabo")  # Output: Hola, Gabo!


# ----------- 6. Funciones con argumentos variables -----------
# Usa `*args` para recibir un número variable de argumentos.

def sumar_todo(*numeros):
    return sum(numeros)

# Llamar a la función con varios números
print(sumar_todo(1, 2, 3, 4))  # Output: 10


# ----------- 7. Funciones con argumentos clave-variable -----------
# Usa `**kwargs` para recibir pares clave-valor.

def detalles(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

# Llamar a la función con argumentos clave-valor
detalles(nombre="Gabo", edad=25, ciudad="México")
# Output:
# nombre: Gabo
# edad: 25
# ciudad: México


# ----------- 8. Ámbito de las variables (local y global) -----------
# Las variables locales existen solo dentro de la función.
# Las variables globales existen fuera de la función y en todo el programa.

# Variable global
x = 10

def ejemplo_ambito():
    x = 5  # Variable local
    print(f"Variable local x: {x}")

ejemplo_ambito()  # Output: Variable local x: 5
print(f"Variable global x: {x}")  # Output: Variable global x: 10


# ----------- 9. Funciones lambda (funciones anónimas) -----------
# Las funciones lambda son funciones pequeñas y rápidas que no tienen nombre.

# Lambda para sumar dos números
suma = lambda a, b: a + b

# Usar la función lambda
print(suma(3, 5))  # Output: 8


# ----------- 10. Documentación en funciones (docstring) -----------
# Puedes agregar una descripción de la función usando cadenas de documentación.

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    :param base: La base del rectángulo.
    :param altura: La altura del rectángulo.
    :return: El área del rectángulo.
    """
    return base * altura

# Llamar a la función y mostrar su documentación
area = calcular_area_rectangulo(5, 10)
print(f"El área del rectángulo es {area}")  # Output: El área del rectángulo es 50
print(calcular_area_rectangulo.__doc__)  # Muestra la documentación


# ----------- 11. Buenas prácticas al usar funciones -----------
# - Usa nombres descriptivos que expliquen lo que hace la función.
# - Divide el código en funciones más pequeñas y reutilizables.
# - Agrega comentarios o docstrings para describir el comportamiento.
# - Evita usar muchas variables globales; usa parámetros y valores de retorno.

# Ejemplo de una función bien estructurada
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo.
    :param radio: El radio del círculo.
    :return: El área del círculo.
    """
    pi = 3.141592653589793
    return pi * (radio ** 2)

# Llamar a la función
area_circulo = calcular_area_circulo(7)
print(f"El área del círculo es {area_circulo:.2f}")  # Output: El área del círculo es 153.94
