import random
import string
import pyperclip     # si el módulo pyperclip no funciona utilizaremos : py -m pip install pyperclip

def generar_contraseña(longitud, usar_mayus, usar_minus, usar_numeros, usar_especiales):
    caracteres = ""
    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_minus:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiales:
        caracteres += string.punctuation

    if not caracteres:
        return "Error: Debes seleccionar al menos un tipo de carácter."

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def menu():
    print("=== Generador Seguro de Contraseñas ===")
    longitud = int(input("Ingresa la longitud de la contraseña: "))
    usar_mayus = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
    usar_minus = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    usar_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

    contraseña = generar_contraseña(longitud, usar_mayus, usar_minus, usar_numeros, usar_especiales)
    print("\nContraseña generada:", contraseña)

    if "Error" not in contraseña:
        copiar = input("¿Deseas copiarla al portapapeles? (s/n): ").lower()
        if copiar == 's':
            pyperclip.copy(contraseña)
            print("¡Contraseña copiada al portapapeles!")

if __name__ == "__main__":
    menu()