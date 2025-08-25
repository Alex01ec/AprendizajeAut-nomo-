import random
import string
import pyperclip # si el módulo pyperclip no funciona utilizaremos : py -m pip install pyperclip

# Diccionario de opciones con el conjunto de caracteres disponibles
TIPOS_CARACTERES = {
    "mayúsculas": string.ascii_uppercase, # Contiene todas las letras del alfabeto en mayúsculas.
    "minúsculas": string.ascii_lowercase, # Contiene todas las letras del alfabeto en minúsculas.
    "números": string.digits,             # Contiene todos los dígitos numéricos.
    "especiales": string.punctuation      # Contiene los caracteres especiales más comunes.
}

# Tupla para validar respuestas de Sí/No
OPCIONES_SI_NO = ("s", "n")

# Lista para guardar el historial de contraseñas generadas en la sesión
historial_contraseñas = []


# Función para generar contraseña
def generar_contraseña(longitud, opciones):
    """
    Genera una contraseña aleatoria en base a las opciones seleccionadas.
    :param longitud: longitud de la contraseña
    :param opciones: lista de claves seleccionadas (ej. ["mayúsculas", "números"])
    :return: contraseña generada o mensaje de error
    """
    caracteres = ""

    # Construcción del conjunto de caracteres usando el diccionario
    for opcion in opciones:
        caracteres += TIPOS_CARACTERES[opcion]

    if not caracteres:
        return "Error: Debes seleccionar al menos un tipo de carácter."

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

    # Guardar en historial (estructura de lista)
    historial_contraseñas.append(contraseña)

    return contraseña


# Función para mostrar el menú y obtener opciones del usuario
def obtener_opciones():
    """
    Pregunta al usuario qué tipos de caracteres quiere usar y devuelve la lista seleccionada.
    :return: lista con las opciones elegidas
    """
    opciones = []
    for tipo in TIPOS_CARACTERES.keys():
        respuesta = input(f"¿Incluir {tipo}? (s/n): ").lower()
        while respuesta not in OPCIONES_SI_NO:
            respuesta = input(f"Opción inválida. ¿Incluir {tipo}? (s/n): ").lower()
        if respuesta == "s":
            opciones.append(tipo)
    return opciones


# Función para mostrar historial
def mostrar_historial():
    """Muestra las contraseñas generadas hasta el momento"""
    print("\n Historial de contraseñas generadas:")
    for i, pwd in enumerate(historial_contraseñas, 1):
        print(f"{i}. {pwd}")


# Función principal
def menu():
    print("=== Generador Seguro de Contraseñas ===")

    while True:
        try:
            longitud = int(input("Ingresa la longitud de la contraseña: "))
        except ValueError:
            print(" Error: Debes ingresar un número entero.")
            continue

        # Obtener las opciones seleccionadas (estructura: lista)
        opciones = obtener_opciones()

        # Generar la contraseña con parámetros
        contraseña = generar_contraseña(longitud, opciones)
        print("\n Contraseña generada:", contraseña)

        if "Error" not in contraseña:
            copiar = input("¿Deseas copiarla al portapapeles? (s/n): ").lower()
            if copiar == "s":
                pyperclip.copy(contraseña)
                print(" ¡Contraseña copiada al portapapeles!")

        # Preguntar si mostrar historial
        ver_historial = input("¿Quieres ver el historial de contraseñas? (s/n): ").lower()
        if ver_historial == "s":
            mostrar_historial()

        # Preguntar si generar otra o salir
        repetir = input("\n¿Deseas generar otra contraseña? (s/n): ").lower()
        if repetir != "s":
            print(" ¡Gracias por usar el generador de contraseñas!")
            break


# Punto de entrada del programa
if __name__ == "__main__":
    menu()
