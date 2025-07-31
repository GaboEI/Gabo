# -*- coding: utf-8 -*-
"""Agenda personal simple para gestionar eventos desde la terminal.

Cada evento registra un nombre, una descripción y la fecha en la que fue
creado. Los eventos previos que solo contaban con descripción seguirán siendo
compatibles, interpretando el nombre como vacío.
"""

import os
import datetime

archivo_eventos = "eventos.txt"


def leer_eventos():
    """Devuelve la lista de eventos almacenados.

    Cada evento es una lista ``[estado, nombre, descripcion, fecha]``. Los
    eventos antiguos sin nombre se representarán con un nombre vacío.
    """
    eventos = []
    if os.path.exists(archivo_eventos):
        with open(archivo_eventos, encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split("|")
                if len(partes) == 4:
                    estado, nombre, descripcion, fecha = partes
                elif len(partes) == 3:
                    estado, descripcion, fecha = partes
                    nombre = ""
                elif len(partes) == 2:
                    estado, descripcion = partes
                    nombre = ""
                    fecha = ""
                else:
                    estado, descripcion = "Pendiente", partes[0]
                    nombre = ""
                    fecha = ""
                eventos.append([estado, nombre, descripcion, fecha])
    return eventos


def guardar_eventos(eventos):
    """Sobrescribe el archivo de eventos con la lista proporcionada."""
    with open(archivo_eventos, "w", encoding="utf-8") as f:
        for evento in eventos:
            if len(evento) == 4:
                estado, nombre, descripcion, fecha = evento
            elif len(evento) == 3:
                estado, descripcion, fecha = evento
                nombre = ""
            else:  # compatibilidad muy antigua
                estado, descripcion = evento
                nombre = ""
                fecha = ""
            f.write(f"{estado}|{nombre}|{descripcion}|{fecha}\n")


def agregar_evento():
    nombre = input("Nombre del evento: ")
    descripcion = input("Describe el nuevo evento: ")
    eventos = leer_eventos()
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    eventos.append(["Pendiente", nombre, descripcion, fecha])
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

    for i, evento in enumerate(eventos, 1):
        est = evento[0]
        nombre = evento[1] if len(evento) > 3 else ""
        desc = evento[2] if len(evento) > 3 else evento[1]
        fecha = evento[3] if len(evento) > 3 else (evento[2] if len(evento) > 2 else "")
        detalle_fecha = f" ({fecha})" if fecha else ""
        titulo = f"{nombre}: {desc}" if nombre else desc
        print(f"[{i}] {titulo}{detalle_fecha} - {est}")


def marcar_completado():
    eventos = leer_eventos()
    if not eventos:
        print("No hay eventos disponibles.")
        return

    for i, evento in enumerate(eventos, 1):
        est = evento[0]
        nombre = evento[1] if len(evento) > 3 else ""
        desc = evento[2] if len(evento) > 3 else evento[1]
        fecha = evento[3] if len(evento) > 3 else (evento[2] if len(evento) > 2 else "")
        detalle_fecha = f" ({fecha})" if fecha else ""
        titulo = f"{nombre}: {desc}" if nombre else desc
        print(f"[{i}] {titulo}{detalle_fecha} - {est}")
    try:
        numero = int(input("Ingresa el número del evento a marcar como completado: "))
        if 1 <= numero <= len(eventos):
            eventos[numero - 1][0] = "Completado"
            guardar_eventos(eventos)
            seleccionado = eventos[numero - 1]
            nombre = seleccionado[1] if len(seleccionado) > 3 else ""
            desc = seleccionado[2] if len(seleccionado) > 3 else seleccionado[1]
            titulo = f"{nombre}: {desc}" if nombre else desc
            print(f"Evento '{titulo}' actualizado a Completado.")
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

    for i, evento in enumerate(eventos, 1):
        est = evento[0]
        nombre = evento[1] if len(evento) > 3 else ""
        desc = evento[2] if len(evento) > 3 else evento[1]
        fecha = evento[3] if len(evento) > 3 else (evento[2] if len(evento) > 2 else "")
        detalle_fecha = f" ({fecha})" if fecha else ""
        titulo = f"{nombre}: {desc}" if nombre else desc
        print(f"[{i}] {titulo}{detalle_fecha} - {est}")
    try:
        numero = int(input("Número del evento a eliminar: "))
        if 1 <= numero <= len(eventos):
            eliminado = eventos.pop(numero - 1)
            guardar_eventos(eventos)
            nombre = eliminado[1] if len(eliminado) > 3 else ""
            desc = eliminado[2] if len(eliminado) > 3 else eliminado[1]
            titulo = f"{nombre}: {desc}" if nombre else desc
            print(f"Evento '{titulo}' eliminado.")
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
