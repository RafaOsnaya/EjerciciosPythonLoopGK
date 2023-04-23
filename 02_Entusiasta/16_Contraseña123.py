# Ejercicio 16: contraseña123

# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.



password = 'contraseña'

pass_in = input('Ingresa la contrasenia: ')

if pass_in.casefold() == password.casefold():
    print("Contrasennia correcta")
else:
    print("Contrasenia incorrecta")