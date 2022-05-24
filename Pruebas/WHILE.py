promedio = 0.0
total = 0
contar = 0
mensaje = "Introduzca la nota de un estudiante (-1 para salir):"

nota = int(input(mensaje))

while nota != -1:
    total = total + nota
    contar = contar + 1
    nota = int(input(mensaje))

promedio = total / contar
print("Promedio de notas del grado escolar es:", promedio)