"""
1. Imprimir un mensaje que indique "Sistema de selección de deporte"
2. Le pida al usuario que indique su género
3. Le soliciteal usuario su edad
4. Le pida tu altura.
5. Si el usuario ingresó "hombre", "masculino" o "varón", le imprima un mensaje que diga: Hombre: True. Caso contrario que indique False.
6. Si el usuario es mayor de edad, que idique Mayor: True, si no False.
7. Si la altura ingresada es superios a los 1,8 metros, indicar Alto: True, caso contrario indicar False.
8. Si el usuario es varón indicar un mensaje que diga "Puede jugar rugby: True", si no False.
9. Si es mujer y es alta, indicar "puede jugar volley: True", caso contrario False.
10. Si es varón alto, imprimir "puede jugar basket: True, sino False.
11. Si es varón menor a 50 año indicar True en puede jugar fútbol, caso contrario indicar false."""

print("Sistema de selección de deporte")
genero = input("Ingrese su género: ").lower()
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura (en metros): "))

es_mayor = edad >= 18
es_varon = genero == "hombre" or genero == "masculino" or genero == "varón"
es_mujer = genero == "mujer" or genero == "femenino" or genero == "chica"
es_alto = altura >= 1.8

juega_rugby = es_varon
juega_voley = es_mujer and es_alto
juega_basquet = es_varon and es_alto
juega_futbol = es_varon and edad < 50

print("Puede jugar rugby: ", es_varon)
print("Puede jugar volley: ", es_mujer and es_alto)
print("Puede jugar basket: ", es_varon and es_alto)
print("Puede jugar futbol: ", es_varon and edad < 50)