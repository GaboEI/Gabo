with open("CURSOS INTEGRADORES DE PROGRAMACIÓN.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()

#lineas = [linea for linea in lineas if linea.strip( ) != ""]

with open("ANEXO PEDAGOGICO.txt", "w", encoding="utf-8") as p1:
    p1.writelines(lineas[15:47])

with open("CURSO INTENSIVO DE C#.txt", "w", encoding="utf-8") as p2:
    p2.writelines(lineas[49:748])

with open("CURSO INTENSIVO DE C++.txt", "w", encoding="utf-8") as p3:
    p3.writelines(lineas[750:1240])

with open("CURSO INTENSIVO PRINCIPAL BASE PYTHON.txt", "w", encoding="utf-8") as p4:
    p4.writelines(lineas[1244:297])

with open("CURSO DE DESAROLLO WEB.txt", "w", encoding="utf-8") as p5:
    p5.writelines(lineas[2908:3090])

with open("CURSO INTENSIVO HTML, CSS y SQL.txt", "w", encoding="utf-8") as p6:
    p6.writelines(lineas[3091:3317])

with open("CURSO INTENSIVO JAVA KOTLIN.txt", "w", encoding="utf-8") as p7:
    p7.writelines(lineas[3319:3616])

with open("CURSO INTENSIVO JAVASCRIPT.txt", "w", encoding="utf-8") as p8:
    p8.writelines(lineas[3618:3803])

with open("CURSO INTENSIVO DE SEGURIDAD INFORMÁTICA Y CIBERSEGURIDAD.txt", "w", encoding="utf-8") as p9:
    p9.writelines(lineas[3806:4364])

with open("CURSO INTENSIVO DE TKINTER.txt", "w", encoding="utf-8") as p10:
    p10.writelines(lineas[4367:4493])

with open("TS CURSO NTENSIVO FULL STACK PRO.txt", "w", encoding="utf-8") as p11:
    p11.writelines(lineas[4495:4700])

with open("CURSO INTENSIVO DE GIT Y GITHUB.txt", "w", encoding="utf-8") as p12:
    p12.writelines(lineas[4707:4810])

with open("CURSO INTENSIVO DE GO.txt", "w", encoding="utf-8") as p13:
    p13.writelines(lineas[4813:4945])

with open("CURSO INTENSIVO DE ESTRUCTURAS DE DATOS Y ALGORITMOS.txt", "w", encoding="utf-8") as p14:
    p14.writelines(lineas[4948:5047])

with open("CURSO INTENSIVO DE ARQUITECTURA DE SOFTWARE Y PATRONES DE DISEÑO.txt", "w", encoding="utf-8") as p15:
    p15.writelines(lineas[5051:5145])

with open("CURSO INTENSIVO INTEGRADOR DE PROGRAMACIÓN Y DESARROLLO PROFESIONAL.txt", "w", encoding="utf-8") as p16:
    p16.writelines(lineas[5149:5327])