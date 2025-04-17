"""
Crear un programa que:
Le pida al usuario que ingrese su nombre.
Le de un mensaje de bienvenida concatenando su nombre al sistema de Garbarino.
Le pida al usuario que indique que opción desea: Comprar electrdomésticos, comprar música o ambos.
En caso que seleccione la primer opción, indicarle que puede comprar una heladera ($50000), 
un TV ($35000) o una licuadora ($5000). El usuario deberá ingresar que desea comprar y 
el sistema almacenar el monto gastado en memoria.
Si selecciona comprar música, indicarle que se poseen los discos de Queen($500), Muse ($300) o 
The Beatles ($450). El usuario deberá seleccionar el disco y el sistema almacenar esa información 
en memoria.
Si el usuario selecciona ambas, el sistema deberá mostrarle primero las opciones  de electrodomésticos 
y luego de música.
Luego el programa deberá indicarle cuál fue el costo total de la compra , darle un mensaje de despedida
 y cerrar su ejecución.
"""


monto_compra = 0

def comprar(precio):
    global monto_compra
    monto_compra += precio

def mostrar_monto(monto_compra):
    print("El total de su compra: $", monto_compra)

def comprar_electro():
    print("Bienvenido a la sección electro de Garbarino")
    opcion = input("""Elija una opción: 
                                        1-> Heladera
                                        2-> TV
                                        3-> Licuadora
                                        4-> salir
                   """)
    if opcion == "1":
        comprar(50000)
    elif opcion == "2":
        comprar(35000)
    elif opcion == "3":
        comprar(5000)
    elif opcion == "4":
        print("Gracias por visitar la sección de electrodomésticos")
        exit()

def comprar_musica():
    print("Bienvenido a la sección música de Garbarino")
    opcion = input("""Elija una opción: 
                                        1-> Queen
                                        2-> Muse
                                        3-> Beatles
                                        4-> salir
                   """)
    if opcion == "1":
        comprar(500)
    elif opcion == "2":
        comprar(300)
    elif opcion == "3":
        comprar(450)
    else:
        print("Gracias por visitar la sección de música")
        exit()


def saludar(nombre):
    if monto_compra > 0:
        print("Hasta pronto, ", nombre ,". Gracias por su compra")
    else:
        print("Hasta pronto, ", nombre)

def menu():
    print("Sistema Garbarino")
    nombre_cliente = input("Ingrese su nombre: ")
    print("Hola" , nombre_cliente , 
          "le damos la bienvenida a Sistema Garbarino")
    opcion = input("""Elija una opción: 
                                        1-> comprar electrodomésticos
                                        2-> comprar música
                                        3-> comprar electrodomésticos y música
                                        4-> salir
                   """)
    if opcion == "1":
        comprar_electro()
        mostrar_monto(monto_compra)
        saludar(nombre_cliente)
    elif opcion == "2":
        comprar_musica()
        mostrar_monto(monto_compra)
        saludar(nombre_cliente)
    elif opcion == "3":
        comprar_electro()
        comprar_musica()
        mostrar_monto(monto_compra)
        saludar(nombre_cliente)
    elif opcion == "4":
        print("Gracias por visitar Garbarino."
        "Hasta pronto")
        exit()
    else:
        print("Opción no válida")
menu()

        


