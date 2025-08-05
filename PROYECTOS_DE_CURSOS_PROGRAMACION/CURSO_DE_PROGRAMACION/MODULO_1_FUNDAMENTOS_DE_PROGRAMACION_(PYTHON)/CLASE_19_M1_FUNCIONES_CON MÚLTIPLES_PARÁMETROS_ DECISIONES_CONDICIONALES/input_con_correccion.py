# input_con_correccion.py
from spellchecker import SpellChecker

# Corrector configurado en español
spell = SpellChecker(language="es")

# Puedes añadir palabras personalizadas si quieres
spell.word_frequency.load_words(["Gabo", "programación", "Python", "OneWin"])

def input_corregido(mensaje):
    entrada = input(mensaje)
    palabras = entrada.strip().lower().split()
    corregidas = [spell.correction(p) for p in palabras]
    return " ".join(corregidas)
