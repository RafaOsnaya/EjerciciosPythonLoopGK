# Ejercicio 27: Tablas de multiplicar

# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.




for i in range(1, 11):
    print("Tabla de multiplicar del", i)
    for j in range(1, 11):
        resultado = i * j
        print(i, "x", j, "=", resultado)
    print()
