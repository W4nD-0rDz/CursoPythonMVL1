#Bucle While
# while numero == 2:
#   print("El número es 2")

numero = 15
while numero > 10:
    print("el número es =", numero)
    numero -= 1

contador = 0
userName = input("Ingrese su nombre de usuario: \n")
password = "XXXXXX"
while contador <= 3 and userName != password:
    password = input("Ingrese su clave de seguridad: \n")
    contador += 1
    print(contador)
    if contador == 3:
        break