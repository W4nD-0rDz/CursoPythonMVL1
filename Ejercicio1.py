# Dé un mensaje de bienvenida que diga “Supermercados La Ilusión”.
# Pedirle al usuario que ingrese su nombre.
# Le pida, concatenando su nombre,  que indique el monto que gastó en el sector verdulería.
# Pedirle que ingrese el monto que gastó en carnicería.
# Que el programa la indique que ingrese lo que gastó en otros sectores.
# En todos los casos anteriores, el usuario podrá ingresar un número entero o decimal.
# Informarle al usuario concatenando su nombre, cuál fue el costo total de su compra.
# Indicarle que tiene un descuento de un 10% e indicarle el monto final con ese beneficio.
# Despedirlo con un mensaje que diga “Gracias por usar nuestro sistema” y cerrar la ejecución del programa.

print("Supermercados La Ilusión\n")
nombre_usuario = input("Por favor, ingrese su nombre\n")
genero_usuario = input("Seleccione (V)arón o (M)ujer\n")
if genero_usuario == "V":
    print("Bienvenido " + nombre_usuario)
elif genero_usuario == "M":
    print("Bienvenida " + nombre_usuario)
else:
    print("Bienvenide " + nombre_usuario)
verduleria = float(input("Por favor indique el monto gastado en verdulería: $"))
carniceria = float(input("Por favor indique el monto gastado en carnicería: $"))
otros = float(input("Por favor indique el monto gastado en otros sectores: $"))
precio_subtotal = verduleria + carniceria + otros
print("")
print(nombre_usuario + ", el precio de su compra es: $" + str(round(precio_subtotal, 2)) + ".")
precio_total = precio_subtotal * 0.9
print("Tu descuento es de 10%, por lo tanto el precio final de tu compra es: $" + str(round(precio_total, 2)))
print("Gracias, " + nombre_usuario + ". Vuelva pronto.\n")
print("Supermercados La Ilusión")