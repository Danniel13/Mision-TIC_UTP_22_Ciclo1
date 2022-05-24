#Ejercicio 3
#1. Diseñe un algoritmo que permita solicitar tanto el 
# nombre como la edad de una persona y posteriormente 
# indicar si es “Mayor de edad” o “Menor de edad” según 
# la información ingresada. Una persona se considera mayor
#  de edad si tiene 18 años o más.

def datos1(nombre: str, edad: int):
  if not isinstance(nombre, str):
    #print (f"El nombre: {nombre} es invalido, Introduzca un nombre válido")
    return f"El nombre: {nombre} es invalido, Introduzca un nombre válido"
  if not isinstance(edad, int):
    #print(f"La edad: {edad} es invalida, introduzca  un valor válido")
    return f"La edad: {edad} es invalida, introduzca  un valor válido"
  if edad < 0:
    #print(f"La edad {edad}, no es valida, debe ser un valor positivo")
    return f"La edad {edad}, no es valida, debe ser un valor positivo"

  if edad >= 18:
    Mensaje= "Mayor de edad"
  else:
    Mensaje= "Menor de edad"
  #print(f"La persona con nombre {nombre}, tiene {edad} años, por lo tanto es {Mensaje}.")
  return f"La persona con nombre {nombre}, tiene {edad} años, por lo tanto es {Mensaje}."
  
datos1("Daniel", 28)



#name = (input ("Por favor introduzca su nombre: "))
#age = (input ("Por favor introduzca su edad: "))


