#Bucle for (recorre solo strings o colecciones)
variable = "letras"
for i in variable:
    print(i)

lista = [1, 2, 3, 4, 5]
for i in lista:
    print(i)

#Estructura de validación típica
emails=["juanito@mail-libre.com.ar", "marito@dogmail-co-uk", "rodri28_en_catmail.de"]
def validar(email):
    for caracter in email:
        if caracter == "@" and caracter==".":
            validacion = True
            break
    else:
        validacion = False
    return validacion

def listarEmailsValidos():
    for mail in emails:
        if validar(mail) == True:
            print(mail, "- dirección válida")
        else:
            print(mail, "- dirección inválida")
    else:
        print("Fin de la lista")
        
listarEmailsValidos()

def adivinarDirector():
    nombreDirector = "Steven Spielberg"
    nombre=input("Ingrese el nombre del director de E.T.\n")

    for i in nombreDirector:
        if nombre == nombreDirector:
            print("Acertaste!!! Ganaste un 50% de descuento")
            descuento = 0.5
        else:
            print("mala suerte. Qué disfrutes tu peli!")
    return descuento

cantidadEntradas = int(input("Elija la cantidad de entradas: "))
for i in range(cantidadEntradas):
    if adivinarDirector() == 0.5:
        break
    else:
        continue

for i in range(2,6):
    print(i)


