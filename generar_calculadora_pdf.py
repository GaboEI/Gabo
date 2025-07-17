import textwrap
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generar_pdf(codigo, explicaciones, nombre_pdf):
    c = canvas.Canvas(nombre_pdf, pagesize=letter)
    width, height = letter
    x_margin = 40
    y = height - 40
    line_height = 14

    c.setFont("Helvetica", 12)
    c.drawString(x_margin, y, "Explicación línea por línea")
    y -= line_height * 2

    for linea, explicacion in zip(codigo, explicaciones):
        texto = f"{linea.rstrip()}  # {explicacion}"
        for line in textwrap.wrap(texto, width=95):
            c.drawString(x_margin, y, line)
            y -= line_height
            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - 40
    c.showPage()
    c.setFont("Helvetica", 12)
    c.drawString(x_margin, height - 40, "Código completo")
    y = height - 60
    for line in codigo:
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 40
        c.drawString(x_margin, y, line.rstrip())
        y -= line_height
    c.save()


def main():
    with open("calculadora.py", "r", encoding="utf-8") as f:
        codigo = f.readlines()

    explicaciones = [
        "Comentario de la cabecera de la calculadora",
        "Nombre del archivo para el historial",
        "",
        "Definición de la función sumar",
        "Devuelve la suma de a y b",
        "",
        "Definición de la función restar",
        "Devuelve la resta de a menos b",
        "",
        "Definición de la función multiplicar",
        "Devuelve la multiplicación de a y b",
        "",
        "Definición de la función dividir",
        "Valida que b no sea cero y retorna la división",
        "",
        "Definición de la función guardar_en_historial",
        "Abre el archivo y guarda la línea recibida",
        "",
        "Definición de ver_historial",
        "Intenta leer e imprimir el archivo de historial",
        "Si el archivo no existe muestra Historial vacío",
        "",
        "Definición de limpiar_historial",
        "Borra el contenido del archivo de historial",
        "",
        "Bloque principal con menú de opciones",
        "Mientras sea True se muestran las opciones",
        "Se solicita una opción al usuario",
        "",
        "Opción 1: Suma con validación de números",
        "Opción 2: Resta con validación de números",
        "Opción 3: Multiplicación con validación de números",
        "Opción 4: División con manejo de error por cero",
        "Opción 5: Mostrar historial",
        "Opción 6: Limpiar historial",
        "Opción 0: Salir del programa",
        "Caso contrario: opción inválida",
    ]

    generar_pdf(codigo, explicaciones, "calculadora_explicacion.pdf")


if __name__ == "__main__":
    main()
