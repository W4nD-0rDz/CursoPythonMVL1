print("hola desde python")
# print(hola) # error
print(2)
print(2+3)

"""Tema: Variables"""
#Int
edad = 27
n1=34
n2=45
n3=8.66

#Float
temp = 35.6
resultado = temp-n1

#bool
valido = True

#Str
nombre = "Lucas"


"""Mostrar"""
print(valido)
print("Temperatura corporal: " + str(temp) + "°C") #para concatenar distintos tipos de variable str(variable Int o Float)
print(nombre + ", " + str(edad))
print(n1/n3)
print(resultado)
print(n1%2) #par
print(n2%2) #impar
print(n1**2) #exponente
print(n2//5) #división que resulta en un Int
print(n1/3) #división que resulta en un Float

"""Declaración de variable por parte del usuario"""
name = input("Ingrese su nombre: ")
surname = input("Indique su apellido: ")
print("Bienvenida/o " + name + " " + surname)

n4=int(input("Ingrese un sumando: "))
n5=int(input("Ingrese un segundo sumando: "))
suma = n4 + n5

print(suma)


