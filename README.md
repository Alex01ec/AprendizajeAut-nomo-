# AprendizajeAut-nomo-
# Ambiente de Desarrollo
Usaremos Python por su simplicidad para lógica de programación.
Herramientas necesarias:
Editor: Visual Studio Code o cualquier editor de texto.
Python: versión 3.13 . 
Librerías:
  random (incluida en Python)
  pyperclip (para copiar al portapapeles) → se instala con: pip install pyperclip
Python es ideal para este proyecto porque permite aplicar conceptos de lógica de programación, ya que su sintaxis es clara y permite enfocarse en los fundamentos como:
# Maejo de Datos 
  a) Variables y Tipos de Datos:
    longitud: tipo int → almacena el número de caracteres deseado para la contraseña.
    usar_mayus, usar_minus, usar_numeros, usar_especiales: tipo bool → indican si se incluirán ciertos caracteres.
    contraseña: tipo str → almacena la contraseña generada.
  b) Inicialización:
    Cada variable se inicializa a partir de entradas del usuario:
    longitud = int(input("Ingresa la longitud: "))
    usar_mayus = input("¿Incluir mayúsculas? (s/n): ") == 's'
# Operaciones Lógicas y Relacionales
  a) Operaciones lógicas (and, or, not):
  Se usan para combinar condiciones:
  if not (usar_mayus or usar_minus or usar_numeros or usar_especiales):
    print("Error: Debes seleccionar al menos un tipo de carácter.")
  b) Operaciones relacionales (==, !=, <, >):
  Comparan valores y controlan decisiones:
  if longitud < 4:
    print("La longitud debe ser mayor o igual a 4")
# Estructuras Condicionales
  Permiten tomar decisiones según las elecciones del usuario:
  if usar_mayus:
    caracteres += string.ascii_uppercase
  También se usan para verificar errores:
  if not caracteres:
    return "Error: Debes seleccionar al menos un tipo de carácter."
# Estructuras Repetitivas
  En este proyecto, la estructura repetitiva while se utiliza para permitir que el usuario genere varias contraseñas sin necesidad de reiniciar el programa manualmente.
  Cómo funciona:
  El while True crea un bucle infinito que mantiene activo el menú principal.
  Dentro del bucle, el programa solicita la longitud y el tipo de caracteres deseados para la contraseña.
  Una vez generada y mostrada la contraseña, se pregunta al usuario si desea generar otra.
  Si responde 's', el bucle continúa y se reinicia el proceso.
  Si responde cualquier otra cosa, se utiliza la instrucción break para salir del bucle y finalizar el programa.

          
# Nota:  Estos conceptos básicos forman la base lógica del sistema.
  
  
