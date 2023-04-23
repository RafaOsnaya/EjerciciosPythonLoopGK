# Ejercicio 26: Triángulo

# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.



numero = int(input("Ingresa un numero entero: "))

for i in range(1, numero + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
