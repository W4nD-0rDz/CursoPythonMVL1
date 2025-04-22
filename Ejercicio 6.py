"""
Desarrollar un juego en Python que:
Le pida al jugador 1 que ingrese un número entre 1 y 10.
Si el número es incorrecto, pedirle que lo ingrese nuevamente hasta que lo haga correctamente.
Indicarle  al jugador 2 que tiene tres chances de adivinar el número del jugador 1 y pedirle que ingrese el número.
A cada intento que no adivina, indicarle que el número no es correcto e informarle cuantos intentos le quedan.
Si adivina, indicarle su puntaje (30 puntos si adivino en el primer intento, 20 si lo adivino en el segundo y 10 si lo adivino en el tercero).
"""

def contar(datosJuego):
    if datosJuego["cuenta"] > 0:
        datosJuego["cuenta"] -= 1
    return datosJuego["cuenta"]

def sumarPuntaje(datosJuego):
    datosJuego["puntaje"] = datosJuego["cuenta"] * 10
    return datosJuego["puntaje"]

def saludar(saludo, datosJuego):
    if saludo == 0:
        print("Bienvenido a adivina-adivinador")
    elif saludo == 1:
        print("Ingrese su nombre")
    elif saludo == 2:
        print("Bienvenido", datosJuego["jugador1"])
    elif saludo == 3:
        print("Bienvenido", datosJuego["jugador2"])
    elif saludo == 4:
        print("Ingrese un número entre 1 y 10")
    elif saludo==5:
        print("El número está fuera de rango. Intente nuevamente.")
    elif saludo == 6:
        print(datosJuego["jugador2"],", no has adivinado. Prueba de nuevo.")
    elif saludo == 7:
        print("¡¡¡Felicitaciones", datosJuego["jugador2"], ", Adivinaste!!!")
    elif saludo == 8:
        print("Tu puntaje es: ", datosJuego["puntaje"], "puntos.")
    elif saludo == 9:
        print("Ya no te quedan intentos. Hasta pronto!")
    elif saludo == 10:
        print("A jugar!!!")
    elif saludo == 11:
        print("Pista: el número es más bajo.")
    elif saludo == 12:
        print("Pista: el número es más alto.")
    elif saludo == 13:
        print("Tenés", datosJuego["cuenta"], "intentos.")

def iniciarJuego():
    datosJuego = {
        "jugador1":"",
        "jugador2":"",
        "numeroSecreto":0,
        "puntaje":0,
        "cuenta":3
    }
    saludar(0, datosJuego)
    saludar(1, datosJuego)
    datosJuego["jugador1"] = input()
    while True:
        saludar(4, datosJuego)
        numero = int(input())
        if 1 <= numero <=10:
            datosJuego["numeroSecreto"] = numero
            break
        else:
            saludar(5, datosJuego)
    saludar(1, datosJuego)
    datosJuego["jugador2"] = input()
    saludar(3, datosJuego)
    return datosJuego

def jugar(datosJuego):
    while datosJuego["cuenta"] > 0:
        saludar(13, datosJuego)
        saludar(10, datosJuego)
        saludar(4, datosJuego)
        numeroJugador2 = int(input())
        if numeroJugador2 == datosJuego["numeroSecreto"]:
            saludar(7, datosJuego)
            datosJuego["puntaje"] = sumarPuntaje(datosJuego)
            saludar(8, datosJuego)
            break
        else:
            contar(datosJuego)
            if datosJuego["cuenta"] > 0:
                if numeroJugador2 > datosJuego["numeroSecreto"]:
                    saludar(11, datosJuego)
                else:
                    saludar(12, datosJuego)
                
                saludar(6, datosJuego)
            else:
                saludar(9, datosJuego)

jugar(iniciarJuego())