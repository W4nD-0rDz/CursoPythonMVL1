"""
Realizar con estas tres listas un programa que:
1. Imprimir el mensaje "Bienvenido al sistema de gestión online de la biblioteca Nacional".
2. Declarar una lista llamada infantiles que contenga los títulos Blancanieves, Los Tres Chanchitos y Cenicienta.
3. Declarar una segunda lista, nombrarla como novelas con los títulos Don Quijote, y La Novicia Revelde.
4. Por último, crear una lista policiales con Sherlock Holmes y Muerte en el Nilo.
5. Le pida al usuario que indique que tarea quiere realizar: 
Ver libros disponibles, eliminar libros,  agregar,  ver el stock de libros o salir del sistema.
6. En caso que la opción ingresada no sea correcta, pedirle nuevamente que ingrese una opción.
7. Si selecciona la opción ver libros, pedirle que ingrese la categoría que desea ver. 
Debe poder ingresar la opción ver todas. 
Imprimirle los títulos correspondientes a la categoría seleccionada.
8. Si ingresa una opción incorrecta, darle la opción que intente nuevamente.
9. Si el usuario selecciona eliminar libros, pedirle el título del libro a borrar. 
En caso que el libro exista, eliminarlo de la lista. 
En caso que no exista, informárselo y pedirle que ingrese otro título.
10. Si desea agregar un libro, pedirle la categoría y el título e ingresarlo. 
En caso que la categoría no exista, informárselo y darle la posibilidad que lo reingrese.
11. Si decide ver el stock, pedirle que ingrese el título e imprimirle cuántos 
ejemplares existen del mismo.
12. Todas las opciones, después de ejecutarse, deben llevar al menu inicial.
"""

infantiles = ["Blancanieves", "Los tres chanchitos", "Cenicienta"]
novelas = ["Don Quijote", "La novicia rebelde"]
policiales = ["Sherlock Holmes", "Muerte en el Nilo"]

def saludar(saludo):
    if saludo == 0:
        print("\nBienvenido al sistema de gestión online de la Biblioteca Nacional.")
    elif saludo == 1:
        print(
                "Para ver los libros disponibles en la colección, presione 1\n" \
                "Para ver la cantidad de cada libro disponible en nuestras colecciones, presione 2\n"
                "Para agregar un libro a una colección, presione 3\n" \
                "Para eliminar un libro de una colección, presione 4\n"
                "Para salir, presione 0"
            )
        print("\n")
    elif saludo == 2:
        print("Seleccione una colección")
    elif saludo == 3:
        print("El libro buscado no se encuentra en ninguna de nuestras colecciones. Intente nuevamente")
        print("\n")
    elif saludo == 4:
        print("Elija una de las siguientes opciones:")
    elif saludo == 5:
        print("Gracias por utilizar el sistema de gestión online de la Biblioteca Nacional.")
        print("\n")
    elif saludo == 6:
        print("Hasta Pronto.")
        print("\n")

def seleccionarLista():
        lista = int(input(
    "1 - infantiles\n" \
    "2 - novelas\n" \
    "3 - policiales\n"
    "0 - ver todas\n"))
        return lista

def verLibros():
    saludar(2)
    lista = seleccionarLista()
    if(lista == 1):
        print("Colección INFANTILES:")
        print("\n".join(infantiles))
        print("\n")
    elif(lista == 2):
        print("\nColección NOVELAS:")
        print("\n".join(novelas))
        print("\n")
    elif(lista == 3):
        print("\nColección POLICIALES:")
        print("\n".join(policiales))
        print("\n")
    elif(lista == 0):
        print("Colección INFANTILES:")
        print("\n".join(infantiles))
        print("\nColección NOVELAS:")
        print("\n".join(novelas))
        print("\nColección POLICIALES:")
        print("\n".join(policiales))
        print("\n")
    else:
        print("Error. Intente nuevamente.")
        print("\n")

def buscarLibro(libro):
    if (libro in infantiles):
        return infantiles
    elif(libro in novelas):
        return novelas
    elif(libro in policiales):
        return policiales
    else:
        saludar(3)

def contarLibro():
    libro = input("Indique el libro que desea revisar: ")
    cantidadLibro = infantiles.count(libro) + novelas.count(libro) + policiales.count(libro)
    if cantidadLibro == 1:
        print("El libro", libro, "aparece un total de", cantidadLibro, "vez en nuestras colecciones.\n")
    elif cantidadLibro > 1 :
        print("El libro", libro, "aparece un total de", cantidadLibro, "veces en nuestras colecciones.\n")
    else:
        saludar(3)

def agregarLibro():
    saludar(2)
    seleccion = seleccionarLista()
    if seleccion == 1:
        libro = input("Indique el libro que desea agregar a la colección: ")
        infantiles.append(libro)
        print("El libro", libro, "ha sido agregado a la colección INFANTILES.\n")
    elif seleccion == 2:
        libro = input("Indique el libro que desea agregar a la colección: ")
        novelas.append(libro)
        print("El libro", libro, "ha sido agregado a la colección NOVELAS.\n")
    elif seleccion == 3:
        libro = input("Indique el libro que desea agregar a la colección: ")
        policiales.append(libro)
        print("El libro", libro, "ha sido agregado a la colección POLICIALES.\n")
    else:
        print("Colección inexistente. Intente nuevamente.")
        agregarLibro()

def eliminarLibro():
    libro = input("Indique qué libro quiere eliminar de la colección: ")
    lista = buscarLibro(libro)
    if lista == infantiles:
        infantiles.remove(libro)
        print("El libro", libro, "ha sido eliminado de la colección INFANTILES.\n")
    elif lista == novelas:
        novelas.remove(libro)
        print("El libro", libro, "ha sido eliminado de la colección NOVELAS.\n")
    elif lista == policiales:
        policiales.remove(libro)
        print("El libro", libro, "ha sido eliminado de la colección POLICIALES.\n")
    else:
        eliminarLibro()

def verMenu():
    saludar(0)
    saludar(4)
    saludar(1)
    seleccion = int(input())
    if seleccion == 1:
        verLibros()
        verMenu()
    elif seleccion == 2:
        contarLibro()
        verMenu()
    elif seleccion == 3:
        agregarLibro()
        verMenu()
    elif seleccion == 4:
        eliminarLibro()
        verMenu()
    elif seleccion == 0:
        saludar(5)
        saludar(6)
        exit()

verMenu()