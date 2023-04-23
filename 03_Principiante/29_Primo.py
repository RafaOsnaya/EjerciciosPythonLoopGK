# Ejercicio 29: Primo

# Escribir un programa que pida al usuario un numero entero y muestre por pantalla si es un numero primo o no.


num = int(input("Ingresa un numero entero: "))
es_primo = True  # Se asume que el numero es primo inicialmente

if num < 2:
    es_primo = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break

if es_primo:
    print(f'{num} es un numero primo')
else:
    print(f'{num} no es un numero primo')
