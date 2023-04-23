# Ejercicio 12: Panaderia

# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.


precio_pz_pan_fresco = 3.49
descuento = 0.6

pz_no_frescas_vendidas = int(input("Ingresa el numero de piezas no frescas vendidas del dia: "))

print(f'Precio habitual de una pieza de pan: {precio_pz_pan_fresco}')
print(f'Descuento pan no fresco: {descuento}%')

precio_regular_total = round(pz_no_frescas_vendidas * precio_pz_pan_fresco,2)
precio_descuento_total = round((pz_no_frescas_vendidas * precio_pz_pan_fresco) * (1-descuento),2)
ahorro = round(precio_regular_total - precio_descuento_total,2)

print(f'Precio habitual por {pz_no_frescas_vendidas}: {precio_regular_total}')
print(f'Precio con descuento del 60%: {precio_descuento_total}')
print(f'Tu Ahorro es de: {ahorro}')