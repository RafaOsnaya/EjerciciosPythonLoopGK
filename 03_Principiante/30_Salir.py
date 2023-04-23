# Ejercicio 30: Salir

# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.


while True:
    entrada = input("Ingresa una cadena de texto o escribe 'salir' para terminar el programa): ")
    if entrada == "salir":
        break
    print(entrada)
