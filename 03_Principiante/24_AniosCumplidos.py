# Ejercicio 24: Años cumplidos

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).



edad = int(input("Ingresa tu edad: "))
anio_actual = 2023

for i in range(1, edad + 1):
    anio_cumplido = anio_actual - edad + i
    print(f'haz cumplido {i} anios en el {anio_cumplido} ')