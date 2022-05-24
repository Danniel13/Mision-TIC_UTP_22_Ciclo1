#Ejercicio 1
#1. Diseñe un algoritmo que reciba una nota definitiva 
# entre 0.0 y 5.0. El algoritmo debe imprimir el valor
#  ingresado, y de ser una nota mayor o igual a 4.0,
#  deberá imprimir un mensaje de felicitaciones.
def nota_final(nota: float):
  #Validación de parametros iniciales:
  if not isinstance(nota, float):
    #print(f"La nota: {nota}, no es un dato valido. Debe ser decimal")
    return f"La nota: {nota}, no es un dato valido. Debe ser decimal"

  if nota < 0.0 or nota > 5.0:
    #print(f"La nota {nota} no esta en el intervalo de 0.0 y 5.0")
    return f"La nota {nota} no esta en el intervalo de 0.0 y 5.0"
  #Procesamiento
  if nota >= 4.0:
    mensaje ="Felicitaciones :v"
  else:
    mensaje="Pailangas"
  #print(f"Su nota definitiva es {nota}, {mensaje}")
  return f"Su nota definitiva es {nota}, {mensaje}"


nota_final(5.0)