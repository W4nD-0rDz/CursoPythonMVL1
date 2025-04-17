#Función: conjunto de líneas de código que se ejecutan en conjunto
print("Sistema de calculadora de promedios")
nombre = input("Ingrese su nombre")

#Esta parte puede convertirse en una función:
materia = input("Ingrese el nombre de la materia")
nota1 = int(input("Ingrese la nota del primer trimestre"))
nota2 = int(input("Ingrese la nota del segundo trimestre"))
nota3 = int(input("Ingrese la nota del tercer trimestre"))
promedio = (nota1 + nota2 + nota3)/3

""" print(nombre , ", tu promedio final de la materia" , materia , "es" , promedio)
if promedio >= 7:
    print("Aprobado")
else:
    print("Desaprobado")"""

#La función (se nombran con verbos en infinitivo) pse definen:
def promediar():
    materia = input("Ingrese el nombre de la materia")
    nota1 = int(input("Ingrese la nota del primer trimestre"))
    nota2 = int(input("Ingrese la nota del segundo trimestre"))
    nota3 = int(input("Ingrese la nota del tercer trimestre"))
    promedio = (nota1 + nota2 + nota3)/3
    return promedio

def aprobar(promedio):
    print(nombre , ", tu promedio final de la materia" , materia , "es" , promedio)
if promedio >= 7:
    print("Aprobado")
else:
    print("Desaprobado")

def calificar():
    promediar()
    aprobar()

opcion = input("Quiere calcular otra materia")
if opcion == "si":
    calificar()
else:
    print("Gracias por usar la calculadora de promedios")

#Otros ejemplos:
n1 = float(input("ingrese un número"))
n2 = float(input("ingrese otro número"))
def sumar():
    global resultado
    resultado = n1 + n2
    return resultado #almacena la respuesta de la función

def ver_regularidad():
    faltas = int("Ingrese la cantidad de faltas")
    if faltas < 5:
        print("Sos regular")
    else:
        print("Has perdido tu regularidad")

nombre = input("Ingrese su nombre")
idioma = input("Indique su idioma")

def saludar(nombre, idioma):
    if idioma == "español":
        print("Hola, ", nombre)
    elif idioma == "ingles":
        print("Hello, ", nombre)
    else:
        print("Disculpas, no hablo" , idioma)
        exit()
   
saludar("Juan", "español")
saludar("James", "ingles")
saludar("Johann", "aleman")

def menu():
    opcion = input("""Indique la acción: 
                                        a->promedio de notas
                                        b->verificar regularidad
                                        c->promedio de notas + regularidad
                                        d->salir
                   """).lower()
    if opcion == "a":
        promediar()
    elif opcion == "b":
        ver_regularidad()
    elif opcion == "c":
        promediar()
        ver_regularidad()
    elif opcion == "d":
        print("Gracias por usar nuestro sistema")
        exit()

#Las funciones se llaman:
promediar()
promedio = promediar() #almacena el resultado
aprobar(promedio) #con un parámetro
aprobar(promediar()) #anidada / recurrente
menu()
valor_total = sumar()
print(sumar())
print(valor_total) 

#variables globales: declaradas dentro del algoritmo (archivo), por fuera de las funciones
                        # puede agregarse "global" al declararla
                        # o agregar return a la salida de la función
#variables locales: declaradas dentro de una función

"""
n1 = float(input("ingrese un número"))
n2 = float(input("ingrese otro número"))
def sumar():
    #global resultado
    resultado = n1 + n2
    return resultado #almacena la respuesta de la función
valor_total = sumar()
print("el total es ", sumar())
print(valor_total)"""

