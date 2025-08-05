"""---------------------------------------------------------------------------------------------------------------------
#todo: Ejercicio 1 - Validar edad del usuario
#!🎯 Objetivo de la clase:                                                                                             
#?	•	Aprender a crear funciones que validen datos antes de procesarlos.
#?	•	Comprender la importancia de validar entradas dentro de funciones.
#?	•	Trabajar con valores de retorno (return) para usar el resultado de una función en otras partes del programa.
#?	•	Reforzar el uso de funciones con parámetros y estructuras condicionales dentro.
------------------------------------------------------------------------------------------------------------------------
#todo 📚 Teoría breve antes de empezar:

#todo 🔹 ¿Qué es una función con validación?

#todo Es una función que verifica que los datos recibidos sean correctos antes de procesarlos. Si no lo son, puede:
	•	Lanzar un mensaje de error.
	•	Devolver un valor por defecto.
	•	Repetir el ingreso hasta que sea válido.


#todo 🔹 ¿Qué es el return?

#todo El return devuelve un valor desde una función al lugar donde fue llamada. Es clave para:
	•	Guardar el resultado.
	•	Usarlo en otra función o parte del programa.
	•	Controlar el flujo del código. 
-----------------------------------------------------------------------------------------------------------------------"""
def solisitar_edad ():
    while True:
        entrada = input("📆ingrese su edad: ")
        if entrada.isdigit(): #! devuelve true si todos los caracteres de la cadena son dijitos
            edad = int(entrada)
            if edad > 0:
                return edad
            else:
                print("⚠️ La edad debe ser mayor que cero")
        else:
            print("⚠️ Ingrese solo numeros positivos")

#* Aqui vamos a llamar a la funcion solisitar_edad:
edad_usuario = solisitar_edad()
print(f"🟢 Edad registrada: {edad_usuario}\n")
print("Fin 👋")



