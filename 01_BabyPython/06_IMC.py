# Ejercicio 6: IMC

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.


peso = float(input("Ingresa tu peso en Kg: "))
estatura = float(input("Ingresa tu peso en metros: "))

imc = round(peso / pow(estatura,2),2) 

print(f"Tu indice de masa corporal es de: {imc}")