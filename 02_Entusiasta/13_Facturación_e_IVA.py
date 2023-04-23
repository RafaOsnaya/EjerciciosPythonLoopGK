# Ejercicio 13: Facturación e IVA

# Utilizando una función, calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicarse un 10%.


#Funcion calcular total con iva
def calcular_total_con_iva(cantidad_sin_iva, porcentaje_iva=10):

    cantidad_con_iva = cantidad_sin_iva * (1 + porcentaje_iva/100)
    return round(cantidad_con_iva,2)

cantidad_sin_iva = float(input("Ingrese el monto total sin IVA: "))
porcentaje_iva = int(input("Ingrese el porcentaje de IVA a aplicar (por defecto es 10%): "))

#factura_final_con_iva= calcular_total_con_iva(cantidad_sin_iva, porcentaje_iva) - creo que esta linea es redundante, no se ya me dio suenio XD
print(f'Total con IVA aplicado: {calcular_total_con_iva(cantidad_sin_iva, porcentaje_iva)}')

