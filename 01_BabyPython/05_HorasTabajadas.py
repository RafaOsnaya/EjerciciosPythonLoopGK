# Ejercicio 5: Horas trabajadas

# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas = input("Cuantas horas trabajaste?: ")
coste = input("Cuanto ganas por hora?: ")

paga = int(horas)*float(coste)

print(f'Tu pago es de: ${paga} por un total de: {horas} horas trabajadas')
