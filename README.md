*Generador Seguro de Contraseñas*

Este proyecto es un generador de contraseñas seguras desarrollado en Python como práctica de la asignatura Lógica de Programación.
El programa permite crear contraseñas aleatorias con opciones de personalización (longitud, tipos de caracteres) y copiar el resultado al portapapeles.
Además, guarda un historial de las contraseñas generadas durante la sesión.

*Características*

Generación de contraseñas seguras con:

  - Letras mayúsculas (A-Z)
  - Letras minúsculas (a-z)
  - Números (0-9)
  - Caracteres especiales (@, #, $, %, etc.)

Definición de la longitud de la contraseña.
Copiado automático al portapapeles.
Historial de contraseñas generadas en la sesión.
Validaciones de entrada y menú interactivo.

*Requisitos*

- Python 3.10 o superior
- Librería externa: pyperclip
Instalar la librería con:
pip install pyperclip

*Ejecución*

Clona este repositorio y ejecuta el archivo principal:

git clone https://github.com/tu-usuario/Generador-Contraseñas.git
cd Generador-Contraseñas
python generador.py

*Uso*
  1. Ingresa la longitud de la contraseña.
  2. Selecciona los tipos de caracteres que deseas incluir (s/n).
  3. Obtén la contraseña generada.
  4. Opcionalmente, cópiala al portapapeles.
  5. Repite el proceso si deseas generar más contraseñas.

Ejemplo de interacción en consola:

=== Generador Seguro de Contraseñas ===

    Ingresa la longitud de la contraseña: 12
    ¿Incluir mayúsculas? (s/n): s
    ¿Incluir minúsculas? (s/n): s
    ¿Incluir números? (s/n): s
    ¿Incluir caracteres especiales? (s/n): n
      Contraseña generada: Ab7fKe9LmPqR
     ¡Contraseña copiada al portapapeles!


*Estructura del código*

Diccionario → Para gestionar los tipos de caracteres.
Lista → Para almacenar el historial de contraseñas.
Tupla → Para validar respuestas s/n.

*Funciones*

  - generar_contraseña(longitud, opciones) → Crea una contraseña según parámetros.
  - obtener_opciones() → Pregunta al usuario qué tipos de caracteres incluir.
  - mostrar_historial() → Muestra las contraseñas generadas en la sesión.
  - menu() → Controla el flujo del programa.

*Objetivo*

Este proyecto fue desarrollado como parte de la asignatura Lógica de Programación en la Universidad Internacional del Ecuador.
Permite aplicar conceptos como:
- Estructuras lógicas (if, else)
- Estructuras repetitivas (while)
- Estructuras de datos (listas, tuplas, diccionarios)
- Modularización y uso de funciones

  



