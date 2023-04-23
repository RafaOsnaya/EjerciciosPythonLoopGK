# Ejercicio 7: Inversor
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.


cantidad_inversion = float(input('Ingresa la cantidad a invertir: '))
interes_anual = float(input('Ingresa el interes anual: '))
num_anios = float(input('Ingresa el numero de anios: ')) #no tengo teclado latinoamericano XD

capital_final = round((cantidad_inversion * pow(1 + interes_anual, num_anios)),2)
ganancia = round((capital_final - cantidad_inversion),2)

print(f'Tu capital final en el lapso de: {num_anios} anios es de: {capital_final} y tus ganancias fueron de $: {ganancia}')
