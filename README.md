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
  Se usa un bucle for para construir la contraseña aleatoria:
  contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
  Este bucle se repite longitud veces y selecciona un carácter al azar en cada iteración.
  También se puede usar un while si se deseamos permitir que el usuario genere varias contraseñas:
  while True:
      menu()
      repetir = input("¿Generar otra contraseña? (s/n): ")
      if repetir != 's':
          break

  Nota: Estos conceptos básicos forman la base lógica del sistema.
  
  
