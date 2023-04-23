# Ejercicio 17: Divisor

# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.



dividendo = float(input("Introduce el dividendo: "))
divisor = float(input("Introduce el divisor: "))


if divisor == 0:
    print("Error!!! -.-: No se puede dividir entre cero")
else:
    resultado = dividendo / divisor
    print(f'El resultado de la division es: {resultado}')
