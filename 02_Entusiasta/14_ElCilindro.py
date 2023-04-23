# Ejercicio 14: El cilindro

# Necesitamos calcular el volumen de un cilindro utilizando primero el resultado de calcular el área de la base, para ello te solicitamos lo hagas creando 2 funciones manejando el resultado final en base a con la primera función obtener el área y que la segunda opere en base al resultado de la primera. No puedes llamar a las 2 funciones en la linea fuera de la declaración de estas, solo puedes llamar a una.


import math

def calcular_area_base(radio):
    area_base = math.pi * pow(radio,2)
    return area_base

def calcular_volumen_cilindro(area_base, altura):
    volumen = area_base * altura
    return volumen

radio = float(input('Ingresa el radio del cilindro: '))
altura = float(input('Ingresa la altura del cilindro: '))

area_base = calcular_area_base(radio)
volumen = calcular_volumen_cilindro(area_base, altura)

print(f'El volumen del cilindro es: {volumen}')