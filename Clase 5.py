#Colecciones (listas, tuplas, conjuntos, diccionarios) almacenan un conjunto de datos

#Listas: tienen un nombre (cammelCase, nombre_lista) en plural
nombresAlumnos=["Juan","Pedro","Pablo","Sergio"]
notasPosibles=[6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
print(nombresAlumnos)
#Los elementos pueden ser de cualquier tipo, en otros lenguajes no es así
datosAlumno=["Juan", "Medina", 33, 7.66, True]
notasAlumnos=[["Juan", 7.66],["Pedro", 4.55],["Pablo", 9.89],["Sergio", 6.66]]
print(notasAlumnos)

#Se pueden realizar operaciones con las listas
datosTurnoTarde = nombresAlumnos + notasAlumnos
print(datosTurnoTarde)

#Los elementos dentro de la lista están indizados
print(nombresAlumnos[2])
print(notasAlumnos[0:2])
print(datosAlumno)
datosAlumno[2]=13
print(datosAlumno)
largoLista= len(nombresAlumnos)
print("La lista de alumnos contiene ", largoLista, "alumnos.")

print(nombresAlumnos[int(len(nombresAlumnos))-1])

#Funciones más empleadas en listas o tuplas:
nombresAlumnos.append("José")
print(nombresAlumnos)
nombresAlumnos.insert(len(nombresAlumnos), "Eustaquio")
print(nombresAlumnos)
nombresAlumnos.extend(["Jaime","Patricio","Torcuato"])
print(nombresAlumnos)
nombresAlumnos.pop()
print(nombresAlumnos)
nombresAlumnos.pop(1)
print(nombresAlumnos)
nombresAlumnos.remove("Jaime")
print(nombresAlumnos)
"""nombresAlumnos("Juan Pablo")
print(nombresAlumnos)"""
print(nombresAlumnos)
nombresAlumnos.sort()
print(nombresAlumnos)
print(notasPosibles)
notasPosibles.sort()
print(notasPosibles)

print(nombresAlumnos)
nombresAlumnos.reverse()
print(nombresAlumnos)
print(notasPosibles)
notasPosibles.reverse()
print(notasPosibles)

indice = nombresAlumnos.index("Patricio")
print("El alumno tiene el número de orden: ", indice)

print("Eustaquio se encuentra en la lista: ", "Eustaquio" in nombresAlumnos)

print("Patricio se encuentra ", nombresAlumnos.count("Patricio"), " veces en la lista")
nombresAlumnos.extend(["Jaime","Patricio","Torcuato"])
print("Ahora Patricio se encuentra ", nombresAlumnos.count("Patricio"), " veces en la lista")

#Importante: diferencia entre del y clear: 
#del borra la lista, clear borra los elementos de la lista
"""print(datosAlumno)
del datosAlumno
datosAlumno.clear()
print(datosAlumno)"""

#Las tuplas se definen con paréntesis. No admiten modificaciones.

alumnasJardin =("Flor", "Flavia", "Fernanda", "Felicitas")
print(alumnasJardin*2)
print(alumnasJardin[2])
alumnasJardin=list(alumnasJardin)





