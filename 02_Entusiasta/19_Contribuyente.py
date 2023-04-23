# Ejercicio 19: Contribuyente

# Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores a 30000 MXN mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.


mayor_edad = 18;
ingreso_mensual = 30000

edad = int(input("Cual es tu edad?: "))
ingreso = int(input("Cual es tu ingreso mensual?: "))

if edad >= mayor_edad and ingreso >= ingreso_mensual:
    print("Ya te toca tributar padrino :(")
else:
    print("Bientos paps, aun no tienes que tributar :)")