#1. Diseñe un algoritmo que reciba una nota
#  definitiva entre 0.0 y 5.0. El algoritmo
#  debe imprimir el valor ingresado, y un
#  mensaje que indique si el estudiante
#  “Ganó el curso” o “Perdió el curso”.
#  Se gana el curso solo si la nota
#  definitiva es mayor o igual a 3.0.


def nota_definitiva(nota_def: float):
  if not isinstance(nota_def, float):
    #print(f"La nota: {nota_def}, no es un dato valido. Debe ser decimal")
    return f"La nota: {nota_def}, no es un dato valido. Debe ser decimal"
  if nota_def < 0.0 or nota_def > 5.0:
    #print(f"La nota: {nota_def} no esta en el intervalo establecido")
    return f"La nota: {nota_def} no esta en el intervalo establecido"
  

  if nota_def >= 3.0:
    mensaje="Ganó el curso"
  else:
    mensaje="Perdió el curso"

  #print(f"El estudiante obtuvo una nota definitiva de: {nota_def}, por lo tanto {mensaje}")
  return f"El estudiante obtuvo una nota definitiva de: {nota_def}, por lo tanto {mensaje}"



nota_definitiva(1.5)


