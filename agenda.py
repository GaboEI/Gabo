import datetime

archivo_eventos = "agenda_gabo.txt"


def registrar_evento():
    fecha_str = input("Fecha y hora (YYYY-MM-DD HH:MM): ")
    try:
        fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Formato de fecha inválido.")
        return
    titulo = input("Título del evento: ")
    descripcion = input("Descripción del evento: ")

    with open(archivo_eventos, "a", encoding="utf-8") as f:
        linea = f"{fecha.isoformat()}|{titulo}|{descripcion}\n"
        f.write(linea)
    print("✅ Evento registrado.")


def leer_eventos():
    eventos = []
    try:
        with open(archivo_eventos, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split("|", 2)
                if len(partes) == 3:
                    fecha = datetime.datetime.fromisoformat(partes[0])
                    titulo = partes[1]
                    descripcion = partes[2]
                    eventos.append((fecha, titulo, descripcion))
    except FileNotFoundError:
        pass
    return sorted(eventos, key=lambda e: e[0])


def ver_eventos():
    eventos = leer_eventos()
    if not eventos:
        print("No hay eventos registrados.")
        return
    for i, (fecha, titulo, descripcion) in enumerate(eventos, 1):
        print(f"[{i}] {fecha:%Y-%m-%d %H:%M} - {titulo}: {descripcion}")


def buscar_evento():
    palabra = input("Palabra clave: ").lower()
    eventos = [e for e in leer_eventos() if palabra in e[1].lower() or palabra in e[2].lower()]
    if not eventos:
        print("No se encontraron coincidencias.")
        return
    for fecha, titulo, descripcion in eventos:
        print(f"{fecha:%Y-%m-%d %H:%M} - {titulo}: {descripcion}")


def eliminar_evento():
    eventos = leer_eventos()
    if not eventos:
        print("No hay eventos para eliminar.")
        return
    ver_eventos()
    try:
        indice = int(input("Número del evento a eliminar: ")) - 1
        if indice < 0 or indice >= len(eventos):
            raise ValueError
    except ValueError:
        print("Índice inválido.")
        return
    eventos.pop(indice)
    with open(archivo_eventos, "w", encoding="utf-8") as f:
        for fecha, titulo, descripcion in eventos:
            f.write(f"{fecha.isoformat()}|{titulo}|{descripcion}\n")
    print("✅ Evento eliminado.")


def exportar_agenda():
    eventos = leer_eventos()
    if not eventos:
        print("No hay eventos para exportar.")
        return
    nombre_archivo = f"agenda_exportada_{datetime.date.today()}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for fecha, titulo, descripcion in eventos:
            f.write(f"{fecha:%Y-%m-%d %H:%M} - {titulo}\n    {descripcion}\n\n")
    print(f"✅ Agenda exportada a {nombre_archivo}.")


# Menú principal
while True:
    print("""
=== AGENDA PERSONAL DE GABO ===
[1] Registrar nuevo evento
[2] Ver todos los eventos
[3] Buscar evento
[4] Eliminar evento
[5] Exportar agenda
[0] Salir
""")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        registrar_evento()
    elif opcion == "2":
        ver_eventos()
    elif opcion == "3":
        buscar_evento()
    elif opcion == "4":
        eliminar_evento()
    elif opcion == "5":
        exportar_agenda()
    elif opcion == "0":
        print("✅ Cerrando agenda. ¡Buen trabajo Gabo!")
        break
    else:
        print("⚠️ Opción inválida.")
