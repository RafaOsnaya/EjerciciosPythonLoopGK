# Ejercicio 11: Cuenta de ahorros

# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.


deposito_inicial = float(input("Ingresa la cantidad a depositar en la cuenta de ahorro: "))
interes = 0.04
balance = deposito_inicial

#Balance primer anio
balance += balance * interes
print(f'Balance primer anio es: {round(balance)}')

#Balance segundo anio
balance += balance * interes
print(f'Balance segundo anio es: {round(balance)}')
2
#Balance tercer anio
balance += balance * interes
print(f'Balance tercer anio es: {round(balance,2)}')