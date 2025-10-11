# cera una funcion que traduzca las letras latinas en codigo morse
def traducir_a_morse(texto):
    codigo_morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-', '&': '.-...', ': ': '---...', '; ': '-.-.-.',
        '=': '-...-', '+': '.-.-.', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
        '!': '-.-.--', '@': '.--.-.', "'": '.----.'
    }
    
    texto = texto.upper()
    morse = ''
    
    for char in texto:
        if char in codigo_morse:
            morse += codigo_morse[char] + ' '
        else:
            morse += char + ' '
    
    return morse.strip()
frase = input("Ingrese una frase para traducir a código morse: ")
morse_traducido = traducir_a_morse(frase)
print("Frase en código morse:", morse_traducido)
