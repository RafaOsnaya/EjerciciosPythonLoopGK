# Ejercicio 8: Juguetería

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

pz_payasos = int(input("Ingresa el numero de payasos vendidos: "))
pz_munecas = int(input("Ingresa el numero de munecas vendidos: "))

peso_payasos = 0.112
peso_munecas = 0.075

peso_total_payasos = pz_payasos * peso_payasos
peso_total_munecas = pz_munecas * peso_munecas

peso_total_paquete = peso_total_payasos + peso_total_munecas
print(f'El peso total del paquete que sera enviado es de: {peso_total_paquete} kg')
