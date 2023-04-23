# Ejercicio 25: Cuenta atrás

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.


numero = int(input("Ingresa un numero entero positivo: "))

if numero < 0:
    print("El numero no es positivo.")
else:
    for i in range(numero, -1, -1):
        if i != 0:
            print(i, end=", ") # end se utiliza para especificar el carácter que se imprimirá después del valor
        else:
            print(i)
