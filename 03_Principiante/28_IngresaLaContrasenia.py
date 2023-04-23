# Ejercicio 28: Ingresa la contraseña

# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


contraseña = "contraseña" 

while True:
    contrasenia_ingresada = input("Introduce la contrasenia: ")
    if contrasenia_ingresada == contraseña:
        print("Contrasenia aceptada - Acceso correcto")
        break
    else:
        print("Contrasenia incorrecta. Vuelve a intentarlo")
