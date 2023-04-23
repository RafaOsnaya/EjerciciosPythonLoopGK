# Ejercicio 10: Diccionario espaniol – ingles


# Crea un diccionario vacio y cargalo conforme el usuario vaya ingresando lo siguiente: 
# una palabra en espaniol y su traduccion al ingles. En pocas palabras, crea tu propio 
# diccionario de palabras en espaniol-ingles.


diccionario = {}

# Funcion para agregar una palabra
def agregar_palabra():
    palabra_es = input('Ingresa tu palabra en espaniol: ')
    palabra_en = input('Ingresa su traduccion en ingles: ')
    diccionario[palabra_es] = palabra_en
    print('Palabra agregada exitosamente.')
    input("")

# Funcion para leer una palabra
def leer_palabra():
    palabra_es = input('Ingresa la palabra en espaniol que deseas leer: ')
    if palabra_es in diccionario:
        print(f"{palabra_es} significa {diccionario[palabra_es]} en ingles.")
        input("")
    else:
        print('La palabra no esta en el diccionario.')
        input("")

# Funcion para actualizar una palabra
def actualizar_palabra():
    palabra_es = input('Ingresa la palabra en espaniol que deseas actualizar: ')
    if palabra_es in diccionario:
        palabra_en = input('Ingresa la nueva traduccion en ingles: ')
        diccionario[palabra_es] = palabra_en
        print('Palabra actualizada exitosamente.')
        input("")
    else:
        print('La palabra no esta en el diccionario.')
        input("")

# Funcion para eliminar una palabra
def borrar_palabra():
    palabra_es = input('Ingresa la palabra en espaniol que deseas eliminar: ')
    if palabra_es in diccionario:
        del diccionario[palabra_es]
        print('Palabra eliminada exitosamente.')
        input("")
    else:
        print('La palabra no esta en el diccionario.')
        input("")

# Funcion para contar palabras en el diccionario
def contar_palabras():
    num_palabras = len(diccionario)
    print(f'Hay {num_palabras} palabras en el diccionario.')
    input("")

#Mostrar palabras del diccionario
def mostrar_palabras(diccionario):
    for palabra_es, palabra_en in diccionario.items():
        print(f"{palabra_es}: {palabra_en}")
        input("")


# Programa principal
while True:
    print('\n Diccionario - Elige una opcion \n')
    print('1. Agregar una palabra')
    print('2. Leer una palabra')
    print('3. Actualizar una palabra')
    print('4. Eliminar una palabra')
    print('5. Contar palabras en el diccionario')
    print('6. Listar palabras en diccionario')
    print('7. Salir\n')
    
    opcion = input('Ingresa el numero de la opcion que deseas: ')
    
    if opcion == '1':
        agregar_palabra()
    elif opcion == '2':
        leer_palabra()
    elif opcion == '3':
        actualizar_palabra()
    elif opcion == '4':
        borrar_palabra()
    elif opcion == '5':
        contar_palabras()
    elif opcion == '6':
        mostrar_palabras(diccionario)
    elif opcion == '7':
        print('Gracias por usar el diccionario. ¡Bye!')
        break
    else:
        print('opcion invalida - Inténtalo nuevamente.')

