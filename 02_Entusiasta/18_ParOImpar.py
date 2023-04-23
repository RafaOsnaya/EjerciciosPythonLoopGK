# Ejercicio 18: ¿Par o impar?
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.


numero = int(input("Introduce un numero entero: "))

if numero % 2 == 0:
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')