# Ejercicio 4: Al revés
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

frase = input("Introduce una frase: ")
frase_invertida = frase[::-1] #La sintaxis [::1] se usa para invertir la cadena de caracteres frase asignada a la variable frase_invertida. Se pueden entender como tres parámetros separados por dos puntos: [inicio:fin:paso]. Al dejar vacío el inicio y el final, se toma toda la cadena de caracteres, mientras que al poner -1 en el paso se indica que se recorre la cadena de forma inversa.
print("Frase invertida:", frase_invertida)
