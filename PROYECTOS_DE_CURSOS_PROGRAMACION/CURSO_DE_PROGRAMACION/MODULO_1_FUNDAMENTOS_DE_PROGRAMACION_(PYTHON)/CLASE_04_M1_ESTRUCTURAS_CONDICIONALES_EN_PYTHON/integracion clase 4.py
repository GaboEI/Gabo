Hernesto = 85
Ramon = 60
Juan = 1000

# notas de la prueva de matematica 3 estudiantes
print("Evaluacion individual")

# Hernesto estudiante 1
print("\nEstudiante 1, puntaje:" , Hernesto)
if Hernesto >= 95:
    print("Exelente")
elif Hernesto >= 85: 
     print("Bien")
elif Hernesto >=75:
    print("Regular")
elif Hernesto >= 60:
    print("Aprobado")
else:
    print("Suspendido")

# Ramon estudiante 2
print("\nEstudiante 2, puntaje:" , Ramon)
if Ramon >= 95:
    print("Exelente")
elif Ramon >= 85: 
     print("Bien")
elif Ramon >=75:
    print("Regular")
elif Ramon >= 60:
    print("Aprobado")
else:
    print("Suspendido")

# Juan estudiante 3
print("\nEstudiante 3, puntaje:" , Juan)
if Juan >= 95:
    print("Exelente")
elif Juan >= 85: 
     print("Bien")
elif Juan >=75:
    print("Regular")
elif Juan >= 60:
    print("Aprobado")
else:
    print("Suspendido")

# Determinación de la nota mayor
print("\nComparacion de los resultados")
if Hernesto >= Ramon and Hernesto >= Juan:
    mejor_resultado = Hernesto
    estudiante = "Hernesto"
elif Ramon >= Hernesto and Ramon >= Juan:
    mejor_resultado = Ramon
    estudiante = "Ramon"
else:
    mejor_resultado = Juan
    estudiante = "Juan"

print(f"\nEl mejor resultado es {mejor_resultado} ,{estudiante}.")
