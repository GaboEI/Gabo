# 🐍 05_menu_modular_con_funciones.py

def mostrar_menu():
    print("\n=== 🌟 MENÚ PRINCIPAL 🌟 ===")
    print("1. 👋 Saludar")
    print("2. 💪 Mostrar mensaje motivacional")
    print("3. 🚪 Salir")
    print("======================")


def pedir_opcion():
    while True:
        try:
            opcion = int(input("➡️ Ingrese una opción (1-3): "))
            if 1 <= opcion <= 3:
                return opcion
            else:
                print("❌ Error: La opción debe estar entre 1 y 3.")
        except ValueError:
            print("❌ Error: Por favor, ingrese un número válido.")


def funcion_opcion_1():
    nombre = input("✍️ Ingrese su nombre: ")
    print(f"👋 ¡Hola, {nombre}! Bienvenido al programa 🎉")


def funcion_opcion_2():
    print("💪 ¡Tú puedes con todo! Sigue adelante y alcanza tus metas 🌟")


def salir():
    print("\n🙏 ¡Gracias por usar el programa! Hasta pronto 😊")


def main():
    while True:
        mostrar_menu()
        opcion = pedir_opcion()
        
        if opcion == 1:
            funcion_opcion_1()
        elif opcion == 2:
            funcion_opcion_2()
        elif opcion == 3:
            salir()
            break


if __name__ == "__main__":
    main()

"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
=== 🌟 MENÚ PRINCIPAL 🌟 ===
1. 👋 Saludar
2. 💪 Mostrar mensaje motivacional
3. 🚪 Salir
======================
➡️ Ingrese una opción (1-3): 1
✍️ Ingrese su nombre: Grabiel Espinosa Izada
👋 ¡Hola, Grabiel Espinosa Izada! Bienvenido al programa 🎉

=== 🌟 MENÚ PRINCIPAL 🌟 ===
1. 👋 Saludar
2. 💪 Mostrar mensaje motivacional
3. 🚪 Salir
======================
➡️ Ingrese una opción (1-3): 2
💪 ¡Tú puedes con todo! Sigue adelante y alcanza tus metas 🌟

=== 🌟 MENÚ PRINCIPAL 🌟 ===
1. 👋 Saludar
2. 💪 Mostrar mensaje motivacional
3. 🚪 Salir
======================
➡️ Ingrese una opción (1-3): 3

🙏 ¡Gracias por usar el programa! Hasta pronto 😊
====================================================================
"""