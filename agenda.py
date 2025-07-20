# -*- coding: utf-8 -*-
"""Agenda personal simple para gestionar eventos desde la terminal."""

import os

archivo_eventos = "eventos.txt"


def leer_eventos():
    """Devuelve la lista de eventos almacenados.

    Cada evento es una lista [estado, descripcion].
    """
    eventos = []
    if os.path.exists(archivo_eventos):
        with open(archivo_eventos, encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split("|", 1)
                if len(partes) == 2:
                    estado, descripcion = partes
                else:
                    estado, descripcion = "Pendiente", partes[0]
                eventos.append([estado, descripcion])
    return eventos


def guardar_eventos(eventos):
    """Sobrescribe el archivo de eventos con la lista proporcionada."""
    with open(archivo_eventos, "w", encoding="utf-8") as f:
        for estado, descripcion in eventos:
            f.write(f"{estado}|{descripcion}\n")


def agregar_evento():
    descripcion = input("Describe el nuevo evento: ")
    eventos = leer_eventos()
    eventos.append(["Pendiente", descripcion])
    guardar_eventos(eventos)
    print("✅ Evento agregado correctamente.")


def ver_eventos(estado="todos"):
    eventos = leer_eventos()
    if estado == "pendientes":
        eventos = [e for e in eventos if e[0] == "Pendiente"]
    elif estado == "completados":
        eventos = [e for e in eventos if e[0] == "Completado"]

    if not eventos:
        print("No hay eventos para mostrar.")
        return

    for i, (est, desc) in enumerate(eventos, 1):
        print(f"[{i}] {desc} - {est}")


def marcar_completado():
    eventos = leer_eventos()
    if not eventos:
        print("No hay eventos disponibles.")
        return

    for i, (est, desc) in enumerate(eventos, 1):
        print(f"[{i}] {desc} - {est}")
    try:
        numero = int(input("Ingresa el número del evento a marcar como completado: "))
        if 1 <= numero <= len(eventos):
            eventos[numero - 1][0] = "Completado"
            guardar_eventos(eventos)
            print("Evento actualizado a Completado.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")


def ver_completados():
    ver_eventos("completados")


def eliminar_evento():
    eventos = leer_eventos()
    if not eventos:
        print("No hay eventos para eliminar.")
        return

    for i, (est, desc) in enumerate(eventos, 1):
        print(f"[{i}] {desc} - {est}")
    try:
        numero = int(input("Número del evento a eliminar: "))
        if 1 <= numero <= len(eventos):
            eliminado = eventos.pop(numero - 1)
            guardar_eventos(eventos)
            print(f"Evento '{eliminado[1]}' eliminado.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")


def menu():
    while True:
        print(
            """
=== Agenda Personal de Gabo ===
[1] Agregar nuevo evento
[2] Ver eventos
[3] Marcar evento como completado
[4] Ver eventos completados
[5] Eliminar evento
[0] Salir
"""
        )
        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_evento()
        elif opcion == "2":
            ver_eventos()
        elif opcion == "3":
            marcar_completado()
        elif opcion == "4":
            ver_completados()
        elif opcion == "5":
            eliminar_evento()
        elif opcion == "0":
            print("👋 Saliendo de la agenda. ¡Hasta pronto, Gabo!")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
