# Ejercicio 21: Sala de juegos

# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 50 MXN y si es mayor de 18 años, 200 MXN


edad = input('Ingresa tu edad: ')

if edad < 4:
    print("Entras gratis ")
elif edad >= 4 or edad <=18:
    print("Pagra 50 MXN")
else:
    print("Paga 200 MXN")