# Ejercicio 22: Pizzeria LoopGk

# La pizzería LoopGk ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

#     Ingredientes vegetarianos: Pimiento y tofu.
#     Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.



opcion = input("¿Desea una pizza vegetariana? (S/N): ")

if opcion == "S":
    print("Ingredientes disponibles:")
    print("1. Pimiento")
    print("2. Tofu")
else:
    print("Ingredientes disponibles:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")

ingrediente = input("Elija un ingrediente (1-3): ")

if opcion == "S":
    tipo_pizza = "vegetariana"
    if ingrediente == "1":
        ingrediente_elegido = "pimiento"
    else:
        ingrediente_elegido = "tofu"
else:
    tipo_pizza = "no vegetariana"
    if ingrediente == "1":
        ingrediente_elegido = "peperoni"
    elif ingrediente == "2":
        ingrediente_elegido = "jamon"
    else:
        ingrediente_elegido = "salmon"

print(f'La pizza elegida es: {tipo_pizza} contiene mozzarella, tomate y su ingrediente especial {ingrediente_elegido}, Buen provecho!')


