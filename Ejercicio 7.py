"""
1.Darle al usuario un mensaje de
bienvenida al Cine La plata y pedirle el correo electrónico.

2.Verificar que el mail contenga un único arroba. 
En caso que así sea indicarle acceso permitido y en caso contrario 
volver a pedirle el correo.

3.Declarar una lista películas que contenga:
“Rambo”, “Nothing Hill” , “Patch Adams “ y “Locademia de Policía”.

4.Pedirle al usuario que indique que película desea ver.  
Mediante un bucle for verificar que la película se encuentre en cartelera. 
En caso que no sea así, mostrarle las películas disponibles 
y pedirle que lo ingrese nuevamente.

5.Pedirle que ingrese la cantidad de entradas que desea e 
informarle el costo total ($1000 por cada entrada adquirida).

6.Informarle al usuario que va a participar de un sorteo en el que tiene 
que adivinar el director de la película ET. 
La cantidad de oportunidades que tiene para adivinarlo corresponderá a la
cantidad de entradas que adquirió.

7.En caso que adivine informarle que tiene un descuento de un 50% y
en caso contrario indicarle que perdió. 

"""
import random

nombreSala = "Cinema La Plata"
cartelera = (
    {"nombre": "Rambo", "director": "Ted Kotcheff"},
    {"nombre": "Nothing Hill", "director": "Roger Michell"},
    {"nombre": "Patch Adams", "director": "Tom Shadyac"},
    {"nombre": "Locademia de Policía", "director": "Hugh Wilson"},
    {"nombre": "E.T.", "director": "Steven Spielberg"}
)
# Función de validación de mail, devuelve la cantidad de arrobas del string
def validarEmail(mail):
    caracterValidador = "@"
    contadorArrobas = 0
    for letra in mail:
        if letra == caracterValidador:
            contadorArrobas +=1
    return contadorArrobas
# función que devuelve un objeto (diccionario) de la cartelera (tupla) 
def buscarPelicula(peliculaBuscada):
    for film in cartelera:
        if peliculaBuscada.lower() == film["nombre"].lower():
            return film
    print(peliculaBuscada.upper(), "no se encuentra disponible en cartelera.")
    return None
#Función que muestra los elementos de la cartelera de forma amigable con el usuario.
def mostrarPeliculas():
    i=1
    for film in cartelera:
        print(i, "-", film["nombre"], "de", film["director"])
        i += 1
#Función que permite elegir una película, tanto por medio de un input del usuario
#como por medio de la selección de uno de los elementos de la cartelera
def elegirPelicula():
    while True:
        peliculaDeseada = input("Indique la película que desea ver: \n")
        peliculaEncontrada = buscarPelicula(peliculaDeseada)
        if peliculaEncontrada:
            return peliculaEncontrada
        else:
            print("Seleccione una de las siguientes: ")
            mostrarPeliculas()
            peliculaElegida = input("Ingrese el número de la película que desea ver: ")
            if peliculaElegida.isdigit():
                indice = int(peliculaElegida)-1
                if 0 <= indice < len(cartelera):
                    return cartelera[indice]
                else:
                    print("Opción fuera de rango. Intente nuevamente.")
            else:
                print("Debe ingresar un número válido. Intente nuevamente.")
#Función que devuelve uno de los objetos (dicc) de la cartelera al azar.
def elegirPeliculaAleatoria():
    return random.choice(cartelera)
#Función que valida la igualdad de dos datos (un string contra un valor dentro de un diccionario)
def verificarDirector(film, director):
    return director.lower().strip() == film["director"].lower()
#Función que modifica un dato dentro de un diccionario, en función de una condición:
# que dos datos sean iguales
def aplicarPromocion(intentos):
    promo = 1
    peliculaAleatoria = elegirPeliculaAleatoria()
    print("Accedé a un 50% de descuento con la trivia de directores.")
    while intentos > 0:
        print("¿Quién es el director de", peliculaAleatoria["nombre"], "?")
        directorElegido = input()
        if verificarDirector(peliculaAleatoria, directorElegido):
            promo = 0.5
            print("Ganaste un 50% de descuento en tu compra. ¡¡¡Felicidades!!!")
            break
        else:
            intentos -= 1
            print("Incorrecto. Te quedan", intentos, "intentos")
    return promo
#Función que muestra los datos contenidos en un diccionario
def mostrarResumen(venta):
    print("\nResumen de la compra:")
    for clave, valor in venta.items():  
        print(f"{clave.capitalize()}: {valor}")
    print("")
#Función que compone el registro de la venta, de acuerdo con las solicitudes del usuario
def venderEntradas():
    venta = {
        "mail":"",
        "pelicula":"",
        "cantidadTickets":0,
        "precioTickets": 1000,
        "promo":1,
        "montoTotal":0
    }
    #Se ejecutan al menos una vez (como un do...while en Java)
    while True:
        mail = input("Ingrese su dirección de correo electrónico: \n")
        if validarEmail(mail) == 1:  
            venta["mail"] = mail
            break
        else:
            print("El correo electrónico ingresado no es válido. Intente nuevamente.")
    while True:
        pelicula = elegirPelicula() 
        if pelicula:
            venta["pelicula"] = pelicula["nombre"]
            break
        else:
            print("No se ha elegido una película. Intente nuevamente.")
    while True:
        cantidad = input("Indique la cantidad de entradas que desea comprar:\n")
        if cantidad.isdigit() and int(cantidad) > 0:
            venta["cantidadTickets"] = int(cantidad)
            break
        else:
            print("Debe ingresar un número válido y mayor a cero.")

    venta["promo"] = aplicarPromocion(venta["cantidadTickets"])
    venta["montoTotal"] = venta["cantidadTickets"] * venta["precioTickets"] * venta["promo"]
    print("El valor de su compra es $",venta["montoTotal"])
    mostrarResumen(venta)
    return venta

def salir():
    print("Gracias por visitar", nombreSala, "\n Hasta pronto!!")
    exit()
#Diccionario que contiene las funcionalidades a las que puede acceder en usuario
menuUsuario = {
    "1": ("Acceder a la boletería", venderEntradas),
    "0": ("Salir", salir)
}
#Función que muestra el diccionario anterior
def mostrarMenuUsuario():
    for opcion, (descripcion, _) in menuUsuario.items():
        print(f"{opcion}. {descripcion}")

#Función que encapsula las funcionalidades del algoritmo
def ejecutarMenuUsuario():
    print("Bienvenido a", nombreSala)
    while True:
        print("Elija una opción de entre las siguientes:")
        mostrarMenuUsuario()
        opcion = input("Opción: ").strip()
        if opcion in menuUsuario:
            _, funcion = menuUsuario[opcion]
            funcion()
            if opcion == "0":
                break
        else:
            print("Opción inválida. Intente nuevamente.")
    
ejecutarMenuUsuario()