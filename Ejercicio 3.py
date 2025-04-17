"""
Crear un programa en python que:
1. De un mensaje de bienvenida que diga "Automotores Carlitos"
2. Le pida al usuario que ingrese el monto que desea gastar.
3. Si el monto es menor a 1000000 le debe indicar que no se tienen autos de ese valor y darle la posibilidad que lo ingrese nuevamente.
4. Le pida al usuario que ingrese la marca que está buscando. En caso que ingrese un valor distinto a Ford o Chevrolet informarle que no 
se trabaja con esa marca y pedirla que la ingrese nuevamente.
5. Le pida al usuario que indique la cantidad de puertas. Si el valor ingresado no está entre 3 y 5 informarle que los autos 
no tienen esa cantidad de puertas y pedirle que reingrese la cantidad de puertas.
6. En todos los casos anteriores, si el usuario ingresa un valor incorrecto por segunda vez, darle un mensaje de despedida 
y cerrar la ejecución del programa.
7. Una vez almacenada la información del monto disponible, la marca y la cantidad de puertas indicarle:
   7.1 Si el monto ingresado es mayor a 5000000, la marca es ford y las puertas son 3 indicarle que se posee la Ford Ranger.
   7.2 Si el monto ingresado es menor a 2000000, la marca es chevrolet y las puertas son 3 o 5 indicarle que tiene disponible el Chevrolet Corsa.
   7.3 Si ingresó Ford de 4 puertas y el valor es menor a 4000000 informarle que se cuenta con la Ford Eco Sport.
   7.4 Si el monto ingresado es mayor a 3000000 y menor a 6000000 y la marca es es Chevrolet informarle que se tiene la Chevrolet Tracker.
   7.5 En cualquier otro caso decirle que no se poseen autos con esas características.
8. Darle al usuario un mensaje de despedida y cerrar la ejecución del programa.
"""

print("Automotores Carlitos")

monto = float(input("Por favor, indique el monto que desea gastar: $"))
if(monto < 1000000):
   print("Lamentablemente no contamos con una oferta en ese monto en este momento. Por favor intente nuevamente.")
   monto = float(input("Indique el monto: $"))
   if(monto < 1000000):
      print("Lamentablemente no contamos con una oferta en ese monto en este momento. Hasta pronto.")
      exit()

marca = input("Por favor, indique la marca deseada: ").lower()
if (marca != "ford" and marca != "chevrolet"):
   print("Lamentablemente no hay disponibilidad de la marca ", marca.upper() , "en este momento. Intente nuevamente.")
   marca = input("Indique la marca: ")
   if (marca != "ford" and marca != "chevrolet"):
      print("Lamentablemente no hay disponibilidad de la marca ", marca.upper() , "Hasta pronto.")
      exit()      
     
puertas = int(input("Indique la cantidad de puertas del vehículo deseado: "))
if puertas < 3 or puertas > 5:
   print("En este momento no hay disponibilidad de vehículos de " , puertas , "puertas. Por favor intente nuevamente.")
   puertas = int(input("Cantidad de puertas: "))
   if puertas < 3 or puertas > 5:
      print("En este momento no hay disponibilidad de vehículos de " , puertas , "puertas. Hasta Pronto.")
      exit()
  
if(monto >= 5000000 and marca == "ford" and puertas == 3):
   print("De acuerdo con lo indicado, ud. puede acceder a una Ford Ranger.")
elif(monto <= 4000000 and marca == "ford" and puertas == 4):
   print("De acuerdo con lo indicado, ud. puede acceder a una Ford Eco Sport.")
elif(3000000 <= monto <=6000000 and marca == "chevrolet"):
   print("De acuerdo con lo indicado, ud. puede acceder a un Chevrolet Tracker")
elif(monto <= 2000000 and marca == "chevrolet" and (puertas == 3 or puertas == 5)):
   print("De acuerdo con lo indicado, ud. puede acceder a un Chevrolet Corsa de" , puertas , "puertas.")
else:
   print("Lamentablemente no contamos con una oferta en ese monto en este momento. Por favor intente nuevamente en el futuro")

print("Gracias por contactar Automotores Carlitos. Hasta pronto.")
exit()